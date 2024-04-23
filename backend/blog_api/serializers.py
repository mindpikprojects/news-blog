from rest_framework import serializers
from .models import Categories, Blog, Advertisement

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class AdvtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = "__all__"