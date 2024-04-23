# blog_api/utils.py
from .models import Blog
from datetime import timedelta
from django.utils import timezone

def update_trending_posts():
    trending_posts = Blog.objects.filter(postlabel__iexact='TRENDING')
    for post in trending_posts:
        if post.time + timedelta(minutes=2) <= timezone.now():  # Adjust timing to 2 minutes
            post.postlabel = 'POPULAR'  # Change the postlabel to 'POPULAR'
            post.save()
