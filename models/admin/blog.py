from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from models.models import Post, PostCategory, CommentPost


@admin.register(CommentPost)
class CommentPostAdmin(admin.ModelAdmin):
    ...


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ['content']
