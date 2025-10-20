from django.contrib import admin
from .models import Article, Comment  # new

class CommentInline(admin.StackedInline):  # new
    model = Comment
    extra = 0 # new

class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [
        CommentInline,
    ]
    list_display = [
        "title",
        "body",
        "author",
    ]

admin.site.register(Article, ArticleAdmin) # new
admin.site.register(Comment)  # new
