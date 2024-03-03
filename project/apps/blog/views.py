from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from . import forms
from . import models
from django.contrib import messages


class PostDetailView(DetailView):
    model = models.Post

    
class PostListView(ListView):
    model = models.Post
    def get_queryset(self):
        if self.request.GET.get("consult"):
            query = self.request.GET.get("consult")
            object_list = models.Post.objects.filter(title__icontains=query)
        else:
            object_list = models.Post.objects.all()
        return object_list

class PostCreateView(LoginRequiredMixin, CreateView):
    model = models.Post
    form_class = forms.PostForm
    success_url = reverse_lazy("blog:post_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "El post se guardó correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
 
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Post
    success_url = reverse_lazy("blog:post_list")

    def get_success_url(self):
            messages.success(self.request, "El post se eliminó correctamente.", extra_tags="alert alert-danger")
            return super().get_success_url()
    

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Post
    success_url = reverse_lazy("blog:post_list")
    form_class = forms.PostForm

    def form_valid(self, form):
        messages.success(self.request, "El post se actualizó correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
 
