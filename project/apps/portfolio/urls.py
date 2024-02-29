from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView.as_view(), name='index'),
    path('management/', views.PortfolioManagementView.as_view(), name='management'),
    # Galleries
    path('tatoo/gallery/', views.TattooGalleryListView.as_view(), name='tattoo_gallery'),
    path('design/gallery/', views.DesignGalleryListView.as_view(), name='design_gallery'),
    # Tattoos
    path("tattoo/detail/<int:pk>", views.TattooDetail.as_view(), name="tattoo_detail"),
    path("tattoo/list/", views.TattooList.as_view(), name="tattoo_list"),
    path("tattoo/create/", views.TattooCreateView.as_view(), name="tattoo_create"),
    path("tattoo/delete/<int:pk>", views.TattooDelete.as_view(), name="tattoo_delete"),
    path("tattoo/update/<int:pk>", views.TattooUpdate.as_view(), name="tattoo_update"),
    # Designs
    path("design/detail/<int:pk>", views.DesignDetail.as_view(), name="design_detail"),
    path("design/list/", views.DesignList.as_view(), name="design_list"),
    path("design/create/", views.DesignCreateView.as_view(), name="design_create"),
    path("design/delete/<int:pk>", views.DesignDelete.as_view(), name="design_delete"),
    path("design/update/<int:pk>", views.DesignUpdate.as_view(), name="design_update"),
    # Messages
    path('message/detail/<int:pk>', views.MessageDetail.as_view(), name='message_detail'),
    path('message/list/', views.MessageList.as_view(), name='message_list'),
    path('message/delete/<int:pk>', views.MessageDelete.as_view(), name='message_delete'),
    path('message/update/<int:pk>', views.MessageUpdate.as_view(), name='message_update'),

]