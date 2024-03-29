from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models


class ReviewDetailView(LoginRequiredMixin, DetailView):
    model = models.Review


class ReviewListView(LoginRequiredMixin, ListView):
    model = models.Review
    paginate_by= 20

    def get_queryset(self):
        if self.request.GET.get("consult"):
            query = self.request.GET.get("consult")
            object_list = models.Review.objects.filter(name__icontains=query).order_by('-id')
        else:
            object_list = models.Review.objects.all().order_by('-id')
        return object_list

class ReviewCreateView(CreateView):
    model = models.Review
    form_class = forms.ReviewForm
    success_url = reverse_lazy("portfolio:index")

    def form_valid(self, form):
        messages.success(self.request, "El comentario se guardó correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    
class ReviewUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        review = get_object_or_404(models.Review, pk=pk)
        if review.aproved:
            review.aproved = False
            messages.success(request, "El comentario se marcó como no aprobado.", extra_tags="alert alert-danger")
        else:
            review.aproved = True
            messages.success(request, "El comentario se marcó como aprobado.", extra_tags="alert alert-success")
        review.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class ReviewDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        review = get_object_or_404(models.Review, pk=pk)
        review.delete()
        messages.success(request, "El comentario se eliminó correctamente.", extra_tags="alert alert-success")
        return redirect('reviews:review_list')