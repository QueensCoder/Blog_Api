from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated


class PostList(generics.ListCreateAPIView):
    # view level permissions
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# if not author post is now read only using permission specified
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # view level permissions
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticated)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
