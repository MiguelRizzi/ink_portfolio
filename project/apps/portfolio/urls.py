from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='portfolio/index.html'), name='index'),
    path('management/', views.PortfolioManagementView.as_view(), name='management'),
    # Tattoos
    path("tattoo/detail/<int:pk>", views.TattooDetail.as_view(), name="tattoo_detail"),
    path("tattoo/list/", views.TattooList.as_view(), name="tattoo_list"),
    path("tattoo/create/", views.TattooCreateView.as_view(), name="tattoo_create"),
    path("tattoo/delete/<int:pk>", views.TattooDelete.as_view(), name="tattoo_delete"),
    path("tattoo/update/<int:pk>", views.TattooUpdate.as_view(), name="tattoo_update"),

]