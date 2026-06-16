# tests/test_me_view.py

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

User = get_user_model()


class MeViewTests(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username="taha",
            email="taha@test.com",
            password="123456"
        )

        # assuming path("me/", MeView.as_view(), name="me")
        self.url = reverse("me")

    def test_authenticated_user_can_get_profile(self):

        self.client.force_authenticate(
            user=self.user
        )

        response = self.client.get(self.url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data["username"],
            self.user.username
        )

        self.assertEqual(
            response.data["email"],
            self.user.email
        )

    def test_unauthenticated_user_gets_401(self):

        response = self.client.get(self.url)

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )