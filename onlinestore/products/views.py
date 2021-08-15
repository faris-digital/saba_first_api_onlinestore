from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse


from .models import Manufacturer, Product


class ManufacturerListView(ListView):
    model = Manufacturer


class ManufacturerDetailView(DetailView):
    model = Manufacturer


def product_list_api(request):
    products = Product.objects.all()
    data = {"products": list(products.values("pk", "name"))}
    return JsonResponse(data)


def product_detail_api(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse(
            {"error": {"code": 404, "message": "Product not found!"}}, status=404
        )

    data = {
        "product": {
            "name": product.name,
            "manufacturer": product.manufacturer.name,
            "description": product.description,
            "price": float(product.price),
            "shipping_cost": float(product.shipping_cost),
            "quantity": product.quantity,
        }
    }
    return JsonResponse(data)
