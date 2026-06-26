from rest_framework.serializers import ModelSerializer
from .models import Category, News, Comment
from django.contrib.auth.models import User

#Class serializers untuk API endpoint get list categories
class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name',)
        
#Class serializers untuk API endpoint get detail categories

class CategoryDetailSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at')
        
#class UserSerializer
class UserSerializer(ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'first_name', 'last_name',)
        
#class commentlist serializer
class CommentListSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'name', 'content', 'created_at',)
        
#class commentformserializer
class CommentFormSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content',)
        
#class news listserializer
class NewsListSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    categories = CategoryListSerializer(many=True, read_only=True)
    
    class Meta:
        model = News
        fields = ('id', 'title', 'excerpt', 'user', 'categories', 'published_at')

#Class Newsdetailserializer
class NewsDetailSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    categories =  CategoryListSerializer(many=True, read_only=True)
    comments = CommentListSerializer(many=True, read_only=True, source='comment_set')
    
    class Meta:
        model = News
        fields = ('id', 'title', 'excerpt', 'content', 'cover', 'published_at', 'user', 'categories', 'comments', )
