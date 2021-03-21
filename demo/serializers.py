from rest_framework import serializers
from .models import AuthUser as User, Post
# from .models import BookNumber, Character, Author, Book

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nume','prenume', 'sex']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title','text', 'good_bad', 'user']

