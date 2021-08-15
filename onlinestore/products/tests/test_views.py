from django.test import TestCase, RequestFactory
from django.urls import reverse


from ..models import Manufacturer
from ..views import ManufacturerListView, ManufacturerDetailView


class ManufacturerViewsTests(TestCase):
    def setUp(self):
        self.maker = Manufacturer.objects.create(name="maker 1", location="here")

    def test_anonymous_access_to_manufacturer_list(self):
        url = reverse("products:manufacturer_list")
        req = RequestFactory().get(url)

        view_fn = ManufacturerListView.as_view()
        res = view_fn(req)

        self.assertEqual(res.status_code, 200)

    def test_anonymous_access_to_manufacturer_details(self):
        url = reverse("products:manufacturer-details", args=[self.maker.pk])
        req = RequestFactory().get(url)

        view_fn = ManufacturerDetailView.as_view()
        res = view_fn(req, pk=self.maker.pk)

        self.assertEqual(res.status_code, 200)
