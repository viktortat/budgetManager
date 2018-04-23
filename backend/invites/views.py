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
        serializer = InvitationSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        wallet = serializer.validated_data.get("wallet", None)
        invited_user_email = serializer.validated_data.get("invited_email", None)
        invited_user = User.objects.filter(email=invited_user_email).first()

        if request.user == invited_user:
            return response.Response(status=status.HTTP_400_BAD_REQUEST, data="You cant invite yourself.")

        if not invited_user:
            return response.Response(status=status.HTTP_404_NOT_FOUND, data="This user does not exist.")

        if not check_wallet_ownership(wallet.id, request.user):
            return response.Response(status=status.HTTP_403_FORBIDDEN, data="This is not your wallet.")

        if Wallet.objects.filter(Q(id=wallet.id) & (Q(owner=invited_user) | Q(users=invited_user))):
            return response.Response(status=status.HTTP_400_BAD_REQUEST, data="User is already member in wallet.")

        if Invitation.objects.filter(Q(invited__email=invited_user_email) & Q(wallet__id=wallet.id) & Q(resolved=False)):
            return response.Response(status=status.HTTP_400_BAD_REQUEST, data="User is already invited.")

        Invitation.objects.create(invited=invited_user, creator=request.user, wallet=wallet)
        return response.Response(status=status.HTTP_201_CREATED)


class ResolveInvitationView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = InvitationSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        invitation_id = serializer.validated_data.get("id", None)
        invitation = Invitation.objects.filter(id=invitation_id).first()

        if not invitation:
            return response.Response(status=status.HTTP_404_NOT_FOUND, data="Invitation does not exist.")

        if invitation.resolved:
            return response.Response(status=status.HTTP_400_BAD_REQUEST, data="Invitation is already resolved.")

        if request.user.is_staff or request.user == invitation.invited:
            invitation.wallet.users.add(invitation.invited)
            invitation.wallet.save()
            invitation.resolved = True
            invitation.save()
            response_text = 'You accepted invitation to wallet: {}'.format(invitation.wallet.name)
            return response.Response(status=status.HTTP_204_NO_CONTENT, data=response_text)

        response_text = "You don't have permission to confirm this invitation."
        return response.Response(status=status.HTTP_403_FORBIDDEN, data=response_text)

    def patch(self, request):
        serializer = InvitationSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        invitation_id = serializer.validated_data.get("id", None)
        invitation = Invitation.objects.filter(id=invitation_id).first()

        if not invitation:
            return response.Response(status=status.HTTP_404_NOT_FOUND, data="Invitation does not exist.")

        if request.user.is_staff or request.user == invitation.invited or request.user == invitation.wallet.owner or request.user == invitation.creator:
            invitation.resolved = True
            invitation.save()
            return response.Response(status=status.HTTP_204_NO_CONTENT)

        response_text = "You don't have permission to cancel this invitation."
        return response.Response(status=status.HTTP_403_FORBIDDEN, data=response_text)
