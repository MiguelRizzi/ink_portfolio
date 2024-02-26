from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class PortfolioManagementView(TemplateView, LoginRequiredMixin):
    template_name = "portfolio/management.html"


