from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path('change_password/', views.CustomPasswordChangeView.as_view(), name='change_password'),
    path("avatar/detail/<int:pk>", views.AvatarDetailView.as_view(), name="avatar_detail"),
    path("avatar/create/", views.AvatarCreateView.as_view(), name="avatar_create"),
    path("avatar/update/<int:pk>", views.AvatarUpdateView.as_view(), name="avatar_update"),
    path("avatar/delete/<int:pk>", views.AvatarDeleteView.as_view(), name="avatar_delete"),
]