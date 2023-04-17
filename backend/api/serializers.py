from drf_extra_fields.fields import Base64ImageField
from posts.models import Comment, Post
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    created = serializers.DateTimeField(read_only=True,format="%b %d, %Y")
    
    class Meta:
        fields = ('id', 'author', 'text', 'created', 'post')
        model = Comment


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    pub_date = serializers.DateTimeField(read_only=True,format="%b %d, %Y")
    image = Base64ImageField()

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'comments')
        model = Post
