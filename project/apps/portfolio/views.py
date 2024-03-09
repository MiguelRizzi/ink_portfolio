from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from . import forms, models
from reviews.models import Review


class indexView(CreateView):
    model = models.Message
    form_class = forms.MessageForm
    success_url = reverse_lazy("portfolio:index")
    template_name="portfolio/index.html"

    def form_valid(self, form):
        messages.success(self.request, "El mensaje se envió correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_list'] = Review.objects.filter(aproved=True)  
        context['tattoo_list'] = models.Tattoo.objects.all()
        context['design_list'] = models.Design.objects.all()
        return context

    

class PortfolioManagementView(TemplateView, LoginRequiredMixin):
    template_name = "portfolio/management.html"


# Tattoo
    
class TattooDetailView(LoginRequiredMixin, DetailView):
    model = models.Tattoo

    

class TattooListView(LoginRequiredMixin, ListView):
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
 

class TattooUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Tattoo
    success_url = reverse_lazy("portfolio:tattoo_list")
    form_class = forms.TattooForm
    def form_valid(self, form):
        messages.success(self.request, "El tatuaje se actualizó correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    

class TattooDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        tattoo = get_object_or_404(models.Tattoo, pk=pk)
        tattoo.delete()
        messages.success(request, "El tatuaje se eliminó correctamente.", extra_tags="alert alert-danger")
        return redirect('portfolio:tattoo_list')   


# Designs
    
class DesignDetailView(LoginRequiredMixin, DetailView):
    model = models.Design


class DesignListView(LoginRequiredMixin, ListView):
    model = models.Design
    def get_queryset(self):
        if self.request.GET.get("consult"):
            query = self.request.GET.get("consult")
            object_list = models.Design.objects.filter(title__icontains=query)
        else:
            object_list = models.Design.objects.all()
        return object_list
    

class DesignCreateView(LoginRequiredMixin, CreateView):
    model = models.Design
    form_class = forms.DesignForm
    success_url = reverse_lazy("portfolio:design_list")
    def form_valid(self, form):
        messages.success(self.request, "El diseño se guardó correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
 
    

class DesignUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Design
    success_url = reverse_lazy("portfolio:design_list")
    form_class = forms.DesignForm
    def form_valid(self, form):
        messages.success(self.request, "El diseño se actualizó correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    

class DesignDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        design = get_object_or_404(models.Design, pk=pk)
        design.delete()
        messages.success(request, "El diseño se eliminó correctamente.", extra_tags="alert alert-danger")
        return redirect('portfolio:design_list') 
    

# Messages
class MessageDetailView(LoginRequiredMixin, DetailView):
    model = models.Message
    def get(self, request, *args, **kwargs):
        previous_url = request.META.get('HTTP_REFERER')
        self.object = self.get_object()
        if not previous_url.endswith(f"message/detail/{self.object.id}"):
            self.object.is_read = True  
            self.object.save()
        return super().get(request, *args, **kwargs)


class MessageListView(LoginRequiredMixin, ListView):
    model = models.Message

    
class MessageUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        message = get_object_or_404(models.Message, pk=pk)
        if message.is_read:
            message.is_read = False
            messages.success(request, "El mensaje se marcó como no leido.", extra_tags="alert alert-danger")
        else:
            message.is_read = True
            messages.success(request, "El mensaje se marcó como leido.", extra_tags="alert alert-success")
        message.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    
class MessageDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        message = get_object_or_404(models.Message, pk=pk)
        message.delete()
        messages.success(request, "El mensaje se eliminó correctamente.", extra_tags="alert alert-danger")
        return redirect('portfolio:message_list') 

    

    # Galleries
class TattooGalleryListView(ListView):
    model = models.Tattoo
    template_name= 'portfolio/tattoo_gallery.html'


        
class DesignGalleryListView(ListView):
    model = models.Design
    template_name= 'portfolio/design_gallery.html'
