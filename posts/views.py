from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
# is authenticated allows users to perform actions if authenticated
from rest_framework.permissions import IsAuthenticated


class PostList(generics.ListCreateAPIView):
    # view level permissions
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# if not author post is now read only using permission specified
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # view level permissions
    permission_classes = (IsAuthorOrReadOnly,)
    # is author or read only does not let test user update post
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
