from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView


urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path('change_password/', views.CustomPasswordChangeView.as_view(), name='change_password'),
    path("avatar/detail/<int:pk>", views.AvatarDetail.as_view(), name="avatar_detail"),
    path("avatar/create/", views.AvatarCreate.as_view(), name="avatar_create"),
    path("avatar/update/<int:pk>", views.AvatarUpdate.as_view(), name="avatar_update"),
    path("avatar/delete/<int:pk>", views.AvatarDelete.as_view(), name="avatar_delete"),
]