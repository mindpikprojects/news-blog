# # myapp/management/commands/update_trending_posts.py
# from django.core.management.base import BaseCommand
# from blog_api.models import Post
# from datetime import timedelta
# from django.utils import timezone

# class Command(BaseCommand):
#     help = 'Updates trending posts'

#     def handle(self, *args, **kwargs):
#         trending_posts = Post.objects.filter(is_trending=True)
#         for post in trending_posts:
#             if post.updated_at + timedelta(hours=2) <= timezone.now():
#                 post.is_trending = False
#                 post.save()
#                 self.stdout.write(self.style.SUCCESS(f"Updated post '{post.title}'"))



# blog_api/management/commands/update_trending_posts.py
from django.core.management.base import BaseCommand
# from blog_api.utils.update_trending_posts
from blog_api.utils import update_trending_posts

class Command(BaseCommand):
    help = 'Updates trending posts'

    def handle(self, *args, **kwargs):
        update_trending_posts()
