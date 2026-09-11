from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,CreateAPIView
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Post, Comment
from .serializer import PostSerializer, CommentSerializer,UserCreateSerializer,UserAuthSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token


# Пагинация
class PostPagination(PageNumberPagination):
    page_size = 5


# GET  /api/v1/posts/
# POST /api/v1/posts/
class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.all()
        return Post.objects.filter(is_published=True)

# GET    /api/v1/posts/{id}/
# PUT    /api/v1/posts/{id}/
# DELETE /api/v1/posts/{id}/
class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# POST /api/v1/posts/{id}/comments/
class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(post_id=self.kwargs['id'],
                        author=self.request.user)


# GET /api/v1/posts/{id}/comments/
class CommentListView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['id'])
#-------------------------------------------------------------------------->

class Restr(APIView):

    def post(self,request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = request.data.get('username') 
        password = request.data.get('password')

        user = User.objects.create_user(
            username=username,
            password=password,
        )

        return Response(status=status.HTTP_201_CREATED,
                    data={'user_id': user.id})

class Login(APIView):

    def post(self,request):
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)  # user / None
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED)