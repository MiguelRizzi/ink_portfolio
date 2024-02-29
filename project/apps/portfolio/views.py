from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from . import forms
from . import models
from django.contrib import messages

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
 

 # Designs
    
class DesignDetail(LoginRequiredMixin, DetailView):
    model = models.Design


class DesignList(LoginRequiredMixin, ListView):
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
 
class DesignDelete(LoginRequiredMixin, DeleteView):
    model = models.Design
    success_url = reverse_lazy("portfolio:design_list")

    def get_success_url(self):
            messages.success(self.request, "El diseño se eliminó correctamente.", extra_tags="alert alert-danger")
            return super().get_success_url()
    

class DesignUpdate(LoginRequiredMixin, UpdateView):
    model = models.Design
    success_url = reverse_lazy("portfolio:design_list")
    form_class = forms.DesignForm

    def form_valid(self, form):
        messages.success(self.request, "El diseño se actualizó correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    
    # Messages
class MessageDetail(LoginRequiredMixin, DetailView):
    model = models.Message

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_read = True  
        self.object.save()
        return super().get(request, *args, **kwargs)


class MessageList(LoginRequiredMixin, ListView):
    model = models.Message

class MessageDelete(LoginRequiredMixin, DeleteView):
    model = models.Message
    success_url = reverse_lazy("portfolio:message_list")

    def get_success_url(self):
            messages.success(self.request, "El mensaje se eliminó correctamente.", extra_tags="alert alert-danger")
            return super().get_success_url()
    

class MessageUpdate(UpdateView):
    model = models.Message
    fields = [] 
    success_url = reverse_lazy('portfolio:message_list')

    def form_valid(self, form):
        instance = form.instance
        
        if instance.is_read:
            instance.is_read = False
            messages.success(self.request, "El mensaje se marcó no como leído.", extra_tags="alert alert-danger")
        else:
            instance.is_read = True
            messages.success(self.request, "El mensaje se marcó como leído.", extra_tags="alert alert-success")
            
        instance.save()
        return super().form_valid(form)

    

    # Galleries
class TattooGalleryListView(ListView):
    model = models.Tattoo
    template_name= 'portfolio/tattoo_gallery.html'


        
class DesignGalleryListView(ListView):
    model = models.Design
    template_name= 'portfolio/design_gallery.html'
