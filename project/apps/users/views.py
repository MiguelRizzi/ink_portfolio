from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from .forms import AvatarForm
from .models import Avatar
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView


# Create your views here.
class AvatarDetail(LoginRequiredMixin, DetailView):
    model = Avatar
    
class AvatarCreate(LoginRequiredMixin, CreateView):
    model = Avatar
    form_class = AvatarForm
    success_url = reverse_lazy('portfolio:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "El avatar se guardó correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
   
    
class AvatarUpdate(LoginRequiredMixin, UpdateView):
    model= Avatar
    form_class = AvatarForm
    success_url = reverse_lazy('portfolio:index')
    def form_valid(self, form):
        messages.success(self.request, "El avatar se actualizó correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)

    
class AvatarDelete(LoginRequiredMixin, DeleteView):
    model= Avatar
    success_url = reverse_lazy("portfolio:index")
    def get_success_url(self):
        messages.success(self.request, "El Avatar se eliminó correctamente.", extra_tags="alert alert-danger")
        return super().get_success_url()
    
class CustomPasswordChangeView(PasswordChangeView):
    template_name="users/change_password.html"
    success_url = reverse_lazy('portfolio:index')