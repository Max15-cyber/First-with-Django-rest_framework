from .models import Post, Category
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from .serializers import PostSerializer, CatSerializer
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication

class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,) - вход по токену

class UpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class DeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnly,)

class CatViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CatSerializer
    permission_classes = (IsAdminUser,)

"""    def get(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset)
        return Response({'posts': serializer.data})
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        return Response({'post': serializer.data})

class UpdateAPIView(generics.UpdateAPIView):
    def put(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data, instance=instance)
        return super().put(request, *args, **kwargs)
 class DeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.get()
    serializer_class = PostSerializer  """



"""class PostAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        return Response({'posts': PostSerializer(posts, many = True).data})
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": 'Method Put Not Allowed'})
        try:
            instance = Post.objects.get(pk = pk)
        except:
            return Response({"error": 'Object does not exist '})
        serializer = PostSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": 'Method Delete Not Allowed'})
        try:
            instance = Post.objects.get(pk = pk)
        except:
            return Response({"error": 'Object does not exist '})
        instance.delete()
        return Response({'post': f'delete post {pk}'})
"""