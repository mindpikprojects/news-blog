from django.shortcuts import render
from .models import Advertisement, Categories, Blog
from .serializers import CategorySerializer, BlogSerializer, AdvtSerializer
from rest_framework import viewsets, pagination
from rest_framework import mixins
from rest_framework.response import Response


# PAGINATION
class BlogPagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 100

class CategoryPostPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100

#################

class BlogApiView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Blog.objects.all().order_by('-id')
    serializer_class = BlogSerializer
    lookup_field = 'slug'
    pagination_class = BlogPagination

class BlogSearchApiView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Blog.objects.all().order_by('-id')
    # queryset = Blog.objects.all().order_by(-id)[1:4]
    serializer_class = BlogSerializer
    lookup_field = 'slug'

class CategoryApiView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

class CategoryPostApiView(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Blog.objects.filter(category=pk)
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)
    
class CatListApiView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'
    
class CategoryPostApiView(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Blog.objects.filter(category=pk)
        paginator = CategoryPostPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = BlogSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class PopularPostsApiView(viewsets.ViewSet):
    def list(self, request, pk=None):
        queryset = Blog.objects.filter(postlabel__iexact='POPULAR').order_by('-id')[0:4]
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)


class TrendingPostsApiView(viewsets.ViewSet):
    def list(self, request, pk=None):
        queryset = Blog.objects.filter(postlabel__iexact='TRENDING').order_by('-id')[0:4]
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)
    

class AdPostApiView(viewsets.ViewSet):
    def list(self, request, pk=None):
        queryset = Advertisement.objects.all()
        serializer = AdvtSerializer(queryset, many=True)
        return Response(serializer.data)
    