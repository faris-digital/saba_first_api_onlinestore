from django.test import TestCase, RequestFactory
from django.urls import reverse


from ..models import Manufacturer, Product
from ..views import (
    ManufacturerListView,
    ManufacturerDetailView,
    product_list_api,
    product_detail_api,
)


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


class ProductAPITests(TestCase):
    def setUp(self):
        self.maker = Manufacturer.objects.create(name="maker 1", location="here")
        self.product = Product.objects.create(
            name="product 1",
            manufacturer=self.maker,
            price=9.99,
            shipping_cost=2.60,
            quantity=10,
        )

    def test_product_list(self):
        url = reverse("products:products-list-api")
        req = RequestFactory().get(url)

        res = product_list_api(req)

        self.assertJSONEqual(
            str(res.content, encoding="utf8"),
            {"products": [{"pk": 1, "name": "product 1"}]},
        )

    def test_product_details(self):
        url = reverse("products:products-detail-api", args=[self.product.pk])
        req = RequestFactory().get(url)

        res = product_detail_api(req, self.product.pk)

        self.assertJSONEqual(
            str(res.content, encoding="utf8"),
            {
                "product": {
                    "name": "product 1",
                    "manufacturer": "maker 1",
                    "description": None,
                    "price": 9.99,
                    "shipping_cost": 2.6,
                    "quantity": 10,
                }
            },
        )

    def test_detail_with_product_not_found(self):
        url = reverse("products:products-detail-api", args=[9999])
        req = RequestFactory().get(url)

        res = product_detail_api(req, 9999)

        self.assertJSONEqual(
            str(res.content, encoding="utf8"),
            {"error": {"code": 404, "message": "Product not found!"}},
        )
        self.assertEqual(res.status_code, 404)
