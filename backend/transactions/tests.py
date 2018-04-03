from django.contrib.auth import get_user_model
from rest_framework import status, test

User = get_user_model()


class TransactionsTests(test.APITestCase):
    def setUp(self):
        User.objects.create_superuser(email='testadmin@example.com', username="testadminusername", password='testpassword')
        User.objects.create_user(email='test@example.com', username="testusername", password='testpassword')

        self.transactions_url = "/api/transactions/"
        self.categories_url = "/api/categories/"
        self.login_url = "/api/auth/login/"

        data = {
            "email": "testadmin@example.com",
            "password": "testpassword"
        }
        response = self.client.post(self.login_url, data, format='json')
        self.token_for_admin = response.data["token"]
        data = {
            "email": "test@example.com",
            "password": "testpassword"
        }
        response = self.client.post(self.login_url, data, format='json')
        self.token_for_user = response.data["token"]
