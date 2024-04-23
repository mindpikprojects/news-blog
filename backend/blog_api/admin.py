from django.contrib import admin
from .models import Categories, Blog, Advertisement


admin.site.site_header = 'Page Seven'
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["id","name"]

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["id","category","title","slug","excerpt","content","content_two","image","author","postlabel"]
    search_fields = ["category"]
    prepopulated_fields = {'slug':('title',)}

@admin.register(Advertisement)
class AdvtAdmin(admin.ModelAdmin):
    list_display = ["id","title","image"]
    prepopulated_fields = {'slug':('title',)}