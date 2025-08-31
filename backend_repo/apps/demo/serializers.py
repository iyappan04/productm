# TODO There's certainly more than one way to do this task, so take your pick.

from rest_framework import serializers
from apps.demo.models import Post, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']   

class PostSerializer(serializers.ModelSerializer):

    user_details = serializers.SerializerMethodField(read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Post
        fields = '__all__'

    def get_user_details(self, obj):
        ser = User.objects.get(id=obj.user.id)
        return UserSerializer(ser, many=False).data
    
    def get_comments(self, obj):
        ser = Comment.objects.filter(post=obj.id)
        return CommentSerializer(ser, many=True).data
    
    
class CommentSerializer(serializers.ModelSerializer):

    user_details = serializers.SerializerMethodField(read_only=True)
    
    # comments = 
    
    class Meta:
        model = Comment
        fields = '__all__'

    def get_user_details(self, obj):
        ser = User.objects.get(id=obj.user.id)
        return UserSerializer(ser, many=False).data
        
        
    