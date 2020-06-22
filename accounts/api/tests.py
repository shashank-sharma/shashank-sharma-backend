from rest_framework.reverse import reverse as api_reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()


class UserTestCase(APITestCase):
    admin_login = {
        'phone_number': '0123456789',
        'password': 'randompassword',
    }

    def setUp(self):
        user_obj1 = User(phone_number='0123456789', email='test1@test.com', is_admin=True)
        user_obj1.set_password('randompassword')
        user_obj1.save()

    def test_user_count(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def get_user_token(self, data):

        url = api_reverse("api-accounts:login")
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data.get('token')

    # Access level for User list
    def test_al_user_list(self):
        url = api_reverse('api-accounts:user-list')
        admin_token = self.get_user_token(self.admin_login)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + admin_token)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
