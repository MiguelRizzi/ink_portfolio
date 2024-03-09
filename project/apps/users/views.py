from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .forms import AvatarForm
from .models import Avatar


# Create your views here.
class AvatarDetailView(LoginRequiredMixin, DetailView):
    model = Avatar
    
class AvatarCreateView(LoginRequiredMixin, CreateView):
    model = Avatar
    form_class = AvatarForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "El avatar se guardó correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('users:avatar_detail', kwargs={'pk': self.object.pk})
   
    
class AvatarUpdateView(LoginRequiredMixin, UpdateView):
    model= Avatar
    form_class = AvatarForm
    success_url = reverse_lazy('portfolio:index')
    def form_valid(self, form):
        messages.success(self.request, "El avatar se actualizó correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('users:avatar_detail', kwargs={'pk': self.object.pk})
    
class AvatarDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        avatar = get_object_or_404(Avatar, pk=pk)
        avatar.delete()
        messages.success(request, "El avatar se eliminó correctamente.", extra_tags="alert alert-danger")
        return redirect('portfolio:index')
    
    
class CustomPasswordChangeView(PasswordChangeView):
    template_name="users/change_password.html"
    success_url = reverse_lazy('portfolio:index')