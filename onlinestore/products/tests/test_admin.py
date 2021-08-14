from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteRegistration(TestCase):
    def setUp(self):
        User = get_user_model()
        self.admin = User.objects.create_superuser("admin", password="changeme")

        self.client = Client()
        self.client.force_login(self.admin)

    def test_manufacturer_model_registered_in_admin_site(self):
        url = reverse("admin:products_manufacturer_changelist")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_products_model_registered_in_admin_site(self):
        url = reverse("admin:products_product_changelist")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
