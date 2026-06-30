#import class untuk view requirement
from django.http import Http404
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#import category model & class serializers untuk model Category
from .models import Category, News, Comment
from .serializers import CategoryListSerializer, CategoryDetailSerializer, NewsListSerializer, NewsDetailSerializer, CommentFormSerializer
from .filters import NewsFilter

#membuat view API Endpoint "Get all categories"
# /api/category
class CategoryListView(ListAPIView):
    #set class serializers
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    )
    
    filter_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']
    ordering = ['created_at']
    #authentication
    permission_classes = (IsAuthenticated,)
    authentication_classes  = [TokenAuthentication]
    

#Membuat view API ENDPOINT /api/category/:id
class CategoryDetailView(RetrieveAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes  = [TokenAuthentication]
    
#Membuat view Get list news
#/api/news
class NewsListView(ListAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.is_published()
    
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )
    filterset_class = NewsFilter
    search_fields = ['title']
    ordering_fields= ['title', 'created_at']
    ordering = ['created_at']
    permission_classes = (IsAuthenticated,)
    authentication_classes  = [TokenAuthentication]
    
#View get detail news
class NewsDetailView(RetrieveAPIView):
    serializer_class = NewsDetailSerializer
    queryset = News.objects.is_published()
    permission_classes = (IsAuthenticated,)
    authentication_classes  = [TokenAuthentication]
    
#View comment on news
class NewsCreateCommentView(CreateAPIView):
    serializer_class = CommentFormSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes  = [TokenAuthentication]
    
    def perform_create(self, serializer):
        news_id = self.kwargs['pk']
        try:
            news = News.objects.get(pk=news_id)
            serializer.save(news_id=news.id)
        except News.DoesNotExist:
            raise Http404

