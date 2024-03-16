from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from . import forms
from . import models


class PostDetailView(DetailView):
    model = models.Post

    
class PostListView(ListView):
    model = models.Post
    paginate_by = 5

    def get_queryset(self):
        if self.request.GET.get("consult"):
            query = self.request.GET.get("consult")
            object_list = models.Post.objects.filter(title__icontains=query).order_by('-created_on')
        else:
            object_list = models.Post.objects.all().order_by('-id')
        return object_list

class PostCreateView(LoginRequiredMixin, CreateView):
    model = models.Post
    form_class = forms.PostForm
    success_url = reverse_lazy("blog:post_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "El post se guardó correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
  

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Post
    success_url = reverse_lazy("blog:post_list")
    form_class = forms.PostForm

    def form_valid(self, form):
        messages.success(self.request, "El post se actualizó correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
 
    
class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        design = get_object_or_404(models.Post, pk=pk)
        design.delete()
        messages.success(request, "La publicacion se eliminó correctamente.", extra_tags="alert alert-danger")
        return redirect('blog:post_list') 
    