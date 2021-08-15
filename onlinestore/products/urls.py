from django.urls import path

from .views import ManufacturerListView, ManufacturerDetailView

app_name = "products"

urlpatterns = [
    path("manufacturer/", ManufacturerListView.as_view(), name="manufacturer_list"),
    path(
        "manufacturer/<int:pk>/",
        ManufacturerDetailView.as_view(),
        name="manufacturer-details",
    ),
]
