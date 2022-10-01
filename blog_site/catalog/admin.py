from django.contrib import admin

# Register your models here.

from .models import Post, Author, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

class CommentInline(admin.TabularInline):
    model =Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish_date']
    list_filter = ['publish_date']
    fields = [('title', 'publish_date'), 'author', 'description']
    inlines = [CommentInline]

class PostInline(admin.TabularInline):
    model =Post

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    inlines = [PostInline]



