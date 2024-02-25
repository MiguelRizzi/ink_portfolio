from django.urls import path
from . import views

urlpatterns = [
   
    path("avatar/detail/<int:pk>", views.AvatarDetail.as_view(), name="avatar_detail"),
    path("avatar/create/", views.AvatarCreate.as_view(), name="avatar_create"),
    path("avatar/update/<int:pk>", views.AvatarUpdate.as_view(), name="avatar_update"),
    path("avatar/delete/<int:pk>", views.AvatarDelete.as_view(), name="avatar_delete"),
]