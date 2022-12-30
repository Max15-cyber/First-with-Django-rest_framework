from .models import Post
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import PostSerializer
from rest_framework.response import Response
from django.forms import model_to_dict
'''
class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.filter(cat_id = 2)
    serializer_class = PostSerializer

'''
class PostAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        return Response({'posts': PostSerializer(posts, many = True).data})
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post_new = Post.objects.create(
            title = request.data['title'],
            content = request.data['content'],
            cat_id = request.data['cat_id']
        )
        return Response({'post': PostSerializer(post_new).data})
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": 'Method Put Not Allowed'})
        try:
            instance = Post.objects.get(pk = pk)
        except:
            return Response({"error": 'Object does not exist '})
        instance.title = request.data['title']
        instance.content = request.data['content']
        instance.cat_id = request.data['cat_id']
        instance.save()
        return Response({'post': request.data})
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": 'Method Delete Not Allowed'})
        try:
            instance = Post.objects.get(pk = pk)
        except:
            return Response({"error": 'Object does not exist '})
        instance.delete()
        return Response({'post': request.data})
