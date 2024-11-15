from django.urls import path
from ventas_app import views

urlpatterns = [
    path("", views.inicio_vista, name="inicio_vista"),
    path("registrarVenta/", views.registrarVenta, name="registrarVenta"),
    path("seleccionarVenta/<codigo>", views.seleccionarVenta, name="selecionarVenta"),
    path("editarVentas/<codigo>", views.editarVentas, name="editarVentas"),
    path("borrarVenta/<codigo>", views.borrarVenta, name="borrarVenta")
    ]
