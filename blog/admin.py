from django.contrib import admin

from auths.admin import UserAdmin
from blog.models import Blogger, Post, Comment, Like, Media

# Register your models here.
@admin.register(Blogger)
class BloggerAdmin(UserAdmin):
    pass

class LikeInline(admin.TabularInline):
    model = Like
    extra = 0

class MediaInline(admin.TabularInline):
    model = Media
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [LikeInline, MediaInline]
    list_display = ("title", "status", "created_at", "last_updated")
    list_filter = ("status", "created_at", "last_updated")
    search_fields = ("title", "body")
    date_hierarchy = "created_at"
    ordering = ("status", "created_at")
    autocomplete_fields = ("blogger",)
    readonly_fields = ("created_at", "last_updated")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("body", "is_deleted", "created_at", "last_updated")
    list_filter = ("is_deleted", "created_at", "last_updated")
    search_fields = ("body",)
    date_hierarchy = "created_at"
    ordering = ("is_deleted", "created_at")
    autocomplete_fields = ("author", "post")
    readonly_fields = ("created_at", "last_updated")
    actions = ["delete_comments"]
