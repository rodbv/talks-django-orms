from django.urls import path

from casas_floripa import views

urlpatterns = [
    path("vendas/", views.vendas, name="vendas"),
]
