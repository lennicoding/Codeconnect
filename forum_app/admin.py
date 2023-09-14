from django.contrib import admin
from .models import Post
from .models import Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'vote_count')

admin.site.register(Post, PostAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)

admin.site.register(Tag, TagAdmin)