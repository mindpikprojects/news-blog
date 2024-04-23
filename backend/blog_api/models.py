from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=225)
    image = models.ImageField(upload_to='image', null=True, blank=True)

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    POST_CHOICES = [
        ('POPULAR', 'popular'),
        ('TRENDING', 'trending'),
    ]
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225)
    excerpt = models.CharField(max_length=225,default="")
    content = models.TextField(null=True, blank=True)
    content_two = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)
    author = models.CharField(max_length=225)
    postlabel = models.CharField(max_length=100, choices=POST_CHOICES, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Advertisement(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225, blank=True)
    url = models.URLField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='ads_image')

    def __str__(self):
        return self.title