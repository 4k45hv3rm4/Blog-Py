from django.contrib import admin
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title','timestamp','updated']
    list_filter  = ['title', 'updated']
    list_display_links = ['updated']
    search_fields = ['title','content']
    list_editable = ['title']
    class Meta:
        model = Post
admin.site.register(Post, PostModelAdmin)
