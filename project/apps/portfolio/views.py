from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from . import forms
from . import models
from django.contrib import messages



class PortfolioManagementView(TemplateView, LoginRequiredMixin):
    template_name = "portfolio/management.html"


# Tattoo
    
class TattooDetail(LoginRequiredMixin, DetailView):
    model = models.Tattoo

    

class TattooList(LoginRequiredMixin, ListView):
    model = models.Tattoo
    def get_queryset(self):
        if self.request.GET.get("consult"):
            query = self.request.GET.get("consult")
            object_list = models.Tattoo.objects.filter(title__icontains=query)
        else:
            object_list = models.Tattoo.objects.all()
        return object_list

class TattooCreateView(LoginRequiredMixin, CreateView):
    model = models.Tattoo
    form_class = forms.TattooForm
    success_url = reverse_lazy("portfolio:tattoo_list")

    def form_valid(self, form):
        messages.success(self.request, "El tatuaje se guardó correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
 
class TattooDelete(LoginRequiredMixin, DeleteView):
    model = models.Tattoo
    success_url = reverse_lazy("portfolio:tattoo_list")

    def get_success_url(self):
            messages.success(self.request, "El tatuaje se eliminó correctamente.", extra_tags="alert alert-danger")
            return super().get_success_url()
    

class TattooUpdate(LoginRequiredMixin, UpdateView):
    model = models.Tattoo
    success_url = reverse_lazy("portfolio:tattoo_list")
    form_class = forms.TattooForm

    def form_valid(self, form):
        messages.success(self.request, "El tatuaje se actualizó correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
 