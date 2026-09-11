from django.urls import path
from .views import (PostListCreateView,PostDetailView,CommentCreateView,CommentListView)

urlpatterns = [
    # Posts
    path('', PostListCreateView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),

    # Comments
    path('posts/<int:id>/comments/create/', CommentCreateView.as_view()),
    path('posts/<int:id>/comments/', CommentListView.as_view()),
]