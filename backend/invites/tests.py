from django.contrib.auth import get_user_model
from rest_framework import status, test
from .models import Invitation

User = get_user_model()


class InvitationTests(test.APITestCase):
    fixtures = ["data_with_invitations.json"]

    def setUp(self):
        self.client = test.APIClient()

        self.get_invitations = "/api/invitations/"
        self.create_invitation = self.get_invitations + "create/"
        self.resolve_invitation = self.get_invitations + "resolve/"

        self.login_url = "/api/auth/login/"

        self.all_users = ["info@lukasfuchs.cz", "panzelva@gmail.com", "lukas.fuchs@email.cz", "mrturtle@lukasfuchs.cz"]
        self.basic_users = ["panzelva@gmail.com", "lukas.fuchs@email.cz", "mrturtle@lukasfuchs.cz"]

        response = self.client.post(self.login_url, data={
            "email": "info@lukasfuchs.cz",
            "password": "testpassword"
        })
        self.token_for_admin = response.data["token"]

        response = self.client.post(self.login_url, data={
            "email": "panzelva@gmail.com",
            "password": "testpassword"
        })
        self.token_for_user_panzelva = response.data["token"]

        response = self.client.post(self.login_url, data={
            "email": "lukas.fuchs@email.cz",
            "password": "testpassword"
        })
        self.token_for_user_lukasfuchs = response.data["token"]

        response = self.client.post(self.login_url, data={
            "email": "mrturtle@lukasfuchs.cz",
            "password": "testpassword"
        })
        self.token_for_user_mrturtle = response.data["token"]

    def test_invitation_creation_by_admin_user(self):
        """
        Admin user must be able to create any invitation
        """
        Invitation.objects.filter(id=1).delete()

        # todo – test if 400 is thrown when user is already in wallet

        for wallet_id in range(1, 4):
            for user_email in self.basic_users:
                data = {
                    "wallet": wallet_id,
                    "invited_id": user_email
                }
                self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_admin)
                response = self.client.post(self.create_invitation, data, format="json")
                print(wallet_id, user_email)
                print(response.data)
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invitation_creation_by_basic_user(self):
        """
        Basic user must be able to create invitations in his wallets

        """
        Invitation.objects.filter(id=1).delete()

        for wallet_id in range(1, 4):
            for user_email in self.basic_users:
                data = {
                    "wallet": wallet_id,
                    "invited_id": user_email
                }
                self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_lukasfuchs)
                response = self.client.post(self.create_invitation, data, format="json")
                if wallet_id == 1:
                    if user_email != "lukas.fuchs@email.cz":
                        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
                    else:
                        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

                self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_panzelva)
                response = self.client.post(self.create_invitation, data, format="json")
                if wallet_id == 2:
                    if user_email != "panzelva@gmail.com":
                        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
                    else:
                        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invitation_creation_by_unauth_user(self):
        """
        Unauth user must NOT be able to create any invitations
        """
        Invitation.objects.filter(id=1).delete()

        for wallet_id in range(1, 4):
            for user_email in self.basic_users:
                data = {
                    "wallet": wallet_id,
                    "invited_id": user_email
                }
                self.client.credentials(HTTP_AUTHORIZATION='JWT ')
                response = self.client.post(self.create_invitation, data, format="json")
                self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
