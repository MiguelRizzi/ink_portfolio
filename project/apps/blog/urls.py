from django.urls import path
from . import views

urlpatterns = [
    path("post/detail/<int:pk>", views.PostDetailView.as_view(), name="post_detail"),
    path("post/list/", views.PostListView.as_view(), name="post_list"),
    path("post/create/", views.PostCreateView.as_view(), name="post_create"),
    path("post/delete/<int:pk>", views.PostDeleteView.as_view(), name="post_delete"),
    path("post/update/<int:pk>", views.PostUpdateView.as_view(), name="post_update"),
]