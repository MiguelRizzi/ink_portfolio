from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from . import forms
from . import models
from django.contrib import messages

# Create your views here.

class ReviewDetailView(LoginRequiredMixin, DetailView):
    model = models.Review


class ReviewListView(LoginRequiredMixin, ListView):
    model = models.Review

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = models.Review
    form_class = forms.ReviewForm
    success_url = reverse_lazy("portfolio:index")

    def form_valid(self, form):
        messages.success(self.request, "La reseña se guardó correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    
class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Review
    success_url = reverse_lazy("reviews:review_list")

    def get_success_url(self):
            messages.success(self.request, "La reseña se eliminó correctamente.", extra_tags="alert alert-danger")
            return super().get_success_url()
    

class ReviewUpdateView(UpdateView):
    model = models.Review
    fields = [] 
    success_url = reverse_lazy('reviews:review_list')
    template_name = "reviews/review_update.html"

    def form_valid(self, form):
        instance = form.instance
        
        if instance.aproved:
            instance.aproved = False
            messages.success(self.request, "La reseña se marcó como aprobada.", extra_tags="alert alert-success")
        else:
            instance.aproved = True
            messages.success(self.request, "La reseña se marcó como no aprobada.", extra_tags="alert alert-danger")
            
        instance.save()
        return super().form_valid(form)