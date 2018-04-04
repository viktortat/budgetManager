from django.contrib.auth import get_user_model
from rest_framework import status, test

User = get_user_model()


class BasicFunctionalityTests(test.APITestCase):
    fixtures = ["testdata.json"]

    def setUp(self):
        """
        User lukasfuchs owns wallets 1 + 3
        User panzelva owns wallets 2 + 3
        """

        self.wallet_url = "/api/wallets/"
        self.wallet_1_url = "/api/wallets/1/"
        self.wallet_2_url = "/api/wallets/2/"
        self.wallet_3_url = "/api/wallets/3/"

        self.categories_url = "/api/categories/"

        self.login_url = "/api/auth/login/"

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

    def test_wallet_creation_by_admin_user(self):
        """
        Admin user must be able to create wallets
        """

        data = {
            "name": "wallet"
        }
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_admin)
        response = self.client.post(self.wallet_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_wallet_creation_by_basic_user(self):
        """ Basic user must be able to create wallets """

        data = {
            "name": "wallet"
        }
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_panzelva)
        response = self.client.post(self.wallet_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_lukasfuchs)
        response = self.client.post(self.wallet_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_wallet_creation_by_unauth_user(self):
        """
        Unauth user must NOT be able to create wallets
        """

        data = {
            "name": "wallet"
        }
        response = self.client.post(self.wallet_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_wallet_read_by_admin_user(self):
        """
        Admin user must be able to read all wallets
        """

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_admin)
        response = self.client.get(self.wallet_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # there are 3 wallets in total

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_admin)
        response = self.client.get(self.wallet_1_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_admin)
        response = self.client.get(self.wallet_2_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_admin)
        response = self.client.get(self.wallet_3_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_wallet_read_by_basic_user(self):
        """
        Basic user must be able to read his owned wallets and wallets where he is in users
        """

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_panzelva)
        response = self.client.get(self.wallet_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # there are 2 wallets for this user

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_panzelva)
        response = self.client.get(self.wallet_1_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_panzelva)
        response = self.client.get(self.wallet_2_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_panzelva)
        response = self.client.get(self.wallet_3_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_lukasfuchs)
        response = self.client.get(self.wallet_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # there are 2 wallets for this user

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_lukasfuchs)
        response = self.client.get(self.wallet_1_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_lukasfuchs)
        response = self.client.get(self.wallet_2_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_lukasfuchs)
        response = self.client.get(self.wallet_3_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_wallet_read_by_unauth_user(self):
        """
        Unauth user must NOT be able to read wallets
        """

        response = self.client.get(self.wallet_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.get(self.wallet_1_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.get(self.wallet_2_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.get(self.wallet_3_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_wallet_patch_by_admin_user(self):
        """
        Admin user must be able to patch all wallets
        """

        data = {
            "name": "wallet"
        }
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_admin)
        response = self.client.patch(self.wallet_1_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "wallet")

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_admin)
        response = self.client.patch(self.wallet_2_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "wallet")

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_admin)
        response = self.client.patch(self.wallet_3_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "wallet")

    def test_wallet_patch_by_basic_user(self):
        """
        Basic user must be able to patch his wallets
        """

        data = {
            "name": "wallet"
        }
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_panzelva)
        response = self.client.patch(self.wallet_1_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_panzelva)
        response = self.client.patch(self.wallet_2_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "wallet")

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_panzelva)
        response = self.client.patch(self.wallet_3_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "wallet")

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_lukasfuchs)
        response = self.client.patch(self.wallet_1_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "wallet")

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_lukasfuchs)
        response = self.client.patch(self.wallet_2_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_lukasfuchs)
        response = self.client.patch(self.wallet_3_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "wallet")

    def test_wallet_patch_by_unauth_user(self):
        """
        Unauth user must NOT be able to patch wallets
        """

        data = {
            "name": "wallet"
        }
        response = self.client.patch(self.wallet_1_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.patch(self.wallet_2_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.patch(self.wallet_3_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_wallet_delete_by_admin_user(self):
        """
        Admin user must be able to delete all wallets
        """

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_admin)
        response = self.client.delete(self.wallet_1_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_admin)
        response = self.client.delete(self.wallet_2_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_admin)
        response = self.client.delete(self.wallet_3_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_wallet_delete_by_basic_user_1(self):
        """
        Basic user must be able to delete all wallets he owns
        """

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_panzelva)
        response = self.client.delete(self.wallet_1_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_panzelva)
        response = self.client.delete(self.wallet_2_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_panzelva)
        response = self.client.delete(self.wallet_3_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_wallet_delete_by_basic_user_2(self):
        """
        Basic user must be able to delete all wallets he owns
        """

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_lukasfuchs)
        response = self.client.delete(self.wallet_1_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_lukasfuchs)
        response = self.client.delete(self.wallet_2_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_lukasfuchs)
        response = self.client.delete(self.wallet_3_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_wallet_delete_by_unauth_user(self):
        """
        Unauth user must NOT be able to delete wallets
        """

        response = self.client.delete(self.wallet_1_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.delete(self.wallet_2_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.delete(self.wallet_3_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_category_creation_by_admin_user(self):
        """
        Admin user must be able to create categories in any wallet
        """

        for wallet_id in range(1, 4):
            data = {
                "name": "category",
                "color": "#FFFFFF",
                "wallet": wallet_id
            }
            self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_admin)
            response = self.client.post(self.categories_url, data, format="json")
            print(response.data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_category_creation_by_basic_user(self):
        """
        Basic user must be able to create categories in his wallets
        """

        for wallet_id in range(1, 4):
            data = {
                "name": "category",
                "color": "#FFFFFF",
                "wallet": wallet_id
            }
            self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_panzelva)
            response = self.client.post(self.categories_url, data, format="json")
            if wallet_id == 1:
                self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
            else:
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        for wallet_id in range(1, 4):
            data = {
                "name": "category",
                "color": "#FFFFFF",
                "wallet": wallet_id
            }
            self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token_for_user_lukasfuchs)
            response = self.client.post(self.categories_url, data, format="json")
            if wallet_id == 2:
                self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
            else:
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_category_creation_by_unauth_user(self):
        """
        Unauth user must NOT be able to create categories in any wallet
        """
        for wallet_id in range(1, 4):
            data = {
                "name": "category",
                "color": "#FFFFFF",
                "wallet": wallet_id
            }
            response = self.client.post(self.categories_url, data, format="json")
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
