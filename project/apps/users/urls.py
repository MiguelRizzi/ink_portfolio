from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView


urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path('change_password/', views.CustomPasswordChangeView.as_view(), name='change_password'),
    path("avatar/detail/<int:pk>", views.AvatarDetailView.as_view(), name="avatar_detail"),
    path("avatar/create/", views.AvatarCreateView.as_view(), name="avatar_create"),
    path("avatar/update/<int:pk>", views.AvatarUpdateView.as_view(), name="avatar_update"),
    path("avatar/delete/<int:pk>", views.AvatarDeleteView.as_view(), name="avatar_delete"),
]