from django.urls import path

from .views import (
    ManufacturerListView,
    ManufacturerDetailView,
    product_list_api,
    product_detail_api,
)

app_name = "products"

urlpatterns = [
    path("manufacturer/", ManufacturerListView.as_view(), name="manufacturer_list"),
    path(
        "manufacturer/<int:pk>/",
        ManufacturerDetailView.as_view(),
        name="manufacturer-details",
    ),
    path("api/products/", product_list_api, name="products-list-api"),
    path("api/products/<int:pk>", product_detail_api, name="products-detail-api"),
]
