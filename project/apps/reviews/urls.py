from django.urls import path
from . import views

urlpatterns = [
    path('review/detail/<int:pk>', views.ReviewDetailView.as_view(), name='review_detail'),
    path('review/list/', views.ReviewListView  .as_view(), name='review_list'),
    path('review/create/', views.ReviewCreateView.as_view(), name='review_create'),
    path('review/delete/<int:pk>', views.ReviewDeleteView.as_view(), name='review_delete'),
    path('review/update/<int:pk>', views.ReviewUpdateView.as_view(), name='review_update'),
]