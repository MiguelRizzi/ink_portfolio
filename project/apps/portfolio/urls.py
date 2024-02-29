from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView.as_view(), name='index'),
    path('management/', views.PortfolioManagementView.as_view(), name='management'),
    # Galleries
    path('tatoo/gallery/', views.TattooGalleryListView.as_view(), name='tattoo_gallery'),
    path('design/gallery/', views.DesignGalleryListView.as_view(), name='design_gallery'),
    # Tattoos
    path("tattoo/detail/<int:pk>", views.TattooDetailView.as_view(), name="tattoo_detail"),
    path("tattoo/list/", views.TattooListView.as_view(), name="tattoo_list"),
    path("tattoo/create/", views.TattooCreateView.as_view(), name="tattoo_create"),
    path("tattoo/delete/<int:pk>", views.TattooDeleteView.as_view(), name="tattoo_delete"),
    path("tattoo/update/<int:pk>", views.TattooUpdateView.as_view(), name="tattoo_update"),
    # Designs
    path("design/detail/<int:pk>", views.DesignDetailView.as_view(), name="design_detail"),
    path("design/list/", views.DesignListView.as_view(), name="design_list"),
    path("design/create/", views.DesignCreateView.as_view(), name="design_create"),
    path("design/delete/<int:pk>", views.DesignDeleteView.as_view(), name="design_delete"),
    path("design/update/<int:pk>", views.DesignUpdateView.as_view(), name="design_update"),
    # Messages
    path('message/detail/<int:pk>', views.MessageDetailView.as_view(), name='message_detail'),
    path('message/list/', views.MessageListView.as_view(), name='message_list'),
    path('message/delete/<int:pk>', views.MessageDeleteView.as_view(), name='message_delete'),
    path('message/update/<int:pk>', views.MessageUpdateView.as_view(), name='message_update'),

]