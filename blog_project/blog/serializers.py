from rest_framework import serializers
from .models import Post, Category
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser



class PostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = ('__all__')



class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


"""class PostModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content"""
"""









class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only = True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.time_create = validated_data.get('time_create', instance.time_create)
        instance.time_update = validated_data.get('time_update', instance.time_update)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.cat_id = validated_data.get('cat_id', instance.cat_id)
        instance.save()
        return instance"""
"""    






def encode():
    model = PostModel('Title 1', 'Post 1')
    model_sr = PostSerializer(model)
    print(model_sr.data)
    print(type(model_sr.data))
    json = JSONRenderer().render(model_sr.data)
    print(json)
    
def decode():
    string = io.BytesIO(b'{"title":"Title 1","content":"Post 1"}')
    print(string)
    data = JSONParser().parse(string)
    print(data)
    serializer = PostSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)"""