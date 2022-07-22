from django.shortcuts import render
from .serializer import PostSerializer, CommentSerializer
from rest_framework.views import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment

class ListPosts(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class ListPopularPosts(ListAPIView):

    queryset = Post.objects.filter(is_popular=True)
    serializer_class = PostSerializer

class ListForYouPosts(ListAPIView):
    
    queryset = Post.objects.filter(is_for_you=True)
    serializer_class = PostSerializer

class Comment(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_queryset(self, **kwargs):
        return self.queryset.filter(id=self.request.kwargs['id'])
