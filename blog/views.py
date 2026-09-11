from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,CreateAPIView
)

from rest_framework.pagination import PageNumberPagination

from .models import Post, Comment
from .serializer import PostSerializer, CommentSerializer
from .permissions import IsOwner


# Пагинация
class PostPagination(PageNumberPagination):
    page_size = 5


# GET  /api/v1/posts/
# POST /api/v1/posts/
class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# GET    /api/v1/posts/{id}/
# PUT    /api/v1/posts/{id}/
# DELETE /api/v1/posts/{id}/
class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwner]


# POST /api/v1/posts/{id}/comments/
class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(post_id=self.kwargs['id'])


# GET /api/v1/posts/{id}/comments/
class CommentListView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['id'])