from decimal import Decimal


from django.test import TestCase


from products.models import Manufacturer, Product


class ManufacturerModelTests(TestCase):
    def setUp(self):
        name = "maker 1"
        location = "somewhere"

        Manufacturer.objects.create(name=name, location=location)

    def test_create_a_manufacturer_instance(self):
        maker = Manufacturer.objects.get(name="maker 1")

        self.assertEqual(maker.name, "maker 1")
        self.assertEqual(maker.description, None)
        self.assertEqual(maker.location, "somewhere")
        self.assertEqual(maker.is_active, True)


class ProductModelTests(TestCase):
    def setUp(self):
        name = "maker 1"
        location = "somewhere"

        maker = Manufacturer.objects.create(name=name, location=location)
        Product.objects.create(
            name="product",
            manufacturer=maker,
            price=10.99,
            shipping_cost=2.60,
            quantity=3,
        )

    def test_create_a_product(self):
        product = Product.objects.get(name="product")

        self.assertEqual(product.name, "product")
        self.assertEqual(product.manufacturer.name, "maker 1")
        self.assertEqual(product.description, None)
        self.assertFalse(product.image)
        self.assertEqual(product.price, Decimal("10.99"))
        self.assertEqual(product.shipping_cost, Decimal("2.60"))
        self.assertEqual(product.quantity, 3)
