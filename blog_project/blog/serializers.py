from rest_framework import serializers
from .models import Post
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
"""
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'cat_id', 'content', 'time_create', 'time_update', 'is_published')

"""

"""class PostModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content"""

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only = True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()
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