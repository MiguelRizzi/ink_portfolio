from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='portfolio/index.html'), name='index'),
    path('management/', views.PortfolioManagementView.as_view(), name='management'),
]