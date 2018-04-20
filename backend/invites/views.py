from django_filters import rest_framework as django_filters
from django.contrib.auth import get_user_model
from django.db.models import Q
from dry_rest_permissions.generics import DRYPermissions
from rest_framework import generics, views, response, status, permissions

from transactions.models import Wallet
from transactions.permissions import check_wallet_ownership
from .filters import InvitationFilter
from .models import Invitation
from .permissions import InvitationFilterBackend
from .serializers import InvitationSerializer

User = get_user_model()


class InvitationListView(generics.ListAPIView):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    permission_classes = [DRYPermissions]
    filter_backends = [InvitationFilterBackend, django_filters.DjangoFilterBackend]
    filter_class = InvitationFilter


class CreateInvitationView(views.APIView):
    """
    User must post email of invited user and wallet id
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user_id = None
        wallet_id = request.data.get("wallet", None)
        invited_user_email = request.data.get("invited_id", None)

        if invited_user_email is not None:
            if str(request.user.email) == str(invited_user_email):
                return response.Response(status=status.HTTP_400_BAD_REQUEST, data="You cant invite yourself.")
            user_qs = User.objects.filter(email=invited_user_email)
            if not user_qs:
                return response.Response(status=status.HTTP_404_NOT_FOUND, data="This user does not exist or you did not provide email.")
            user_id = user_qs.first().id

        serializer = InvitationSerializer(data={'invited_id': user_id, 'wallet': wallet_id, 'status': 'pending'})
        serializer.is_valid(raise_exception=True)

        if wallet_id is not None:
            if not check_wallet_ownership(wallet_id, request.user):
                return response.Response(status=status.HTTP_403_FORBIDDEN, data="This is not your wallet.")

        if wallet_id is not None and invited_user_email is not None:
            invited_user = User.objects.filter(email=invited_user_email).first()
            if Wallet.objects.filter(Q(id=wallet_id) & (Q(owner=invited_user) | Q(users=invited_user))):
                return response.Response(status=status.HTTP_400_BAD_REQUEST, data="User is already member in wallet.")

            if Invitation.objects.filter(Q(invited__email=invited_user_email) & Q(wallet__id=wallet_id) & Q(status="pending")):
                return response.Response(status=status.HTTP_400_BAD_REQUEST, data="User is already invited.")

        serializer.save(creator=request.user)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)


class ResolveInvitationView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    options = ['accepted', 'refused', 'canceled']

    def post(self, request):
        serializer = InvitationSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        invitation_id = serializer.validated_data.get('id', None)
        invitation_status = serializer.validated_data.get('status', None)

        if invitation_status not in self.options:
            response_text = "Status '{}' is not valid.".format(invitation_status)
            return response.Response(status=status.HTTP_400_BAD_REQUEST, data=response_text)

        invitation = Invitation.objects.filter(id=invitation_id).first()
        if not invitation:
            response_text = "Invitation with id '{}' not found.".format(invitation_id)
            return response.Response(status=status.HTTP_404_NOT_FOUND, data=response_text)

        if not check_wallet_ownership(invitation.wallet.id, request.user):
            response_text = "You dont have rights to edit this invitation."
            return response.Response(status=status.HTTP_404_NOT_FOUND, data=response_text)

        return response.Response(status=status.HTTP_200_OK)
