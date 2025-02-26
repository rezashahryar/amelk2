from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('list/', views.PostListView.as_view(), name='blog_list'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('add/comment/<int:pk>/', views.add_comment_post_view, name='add_comment_post'),
]

