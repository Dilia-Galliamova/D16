from django.contrib import admin
from .models import Category, Author, Post, Comment


def nullfy_rating(modeladmin, request, queryset):
    queryset.update(rating=0)
nullfy_rating.short_description = 'Обнулить рейтинг'

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'type', 'rating', 'create_time', 'text')
    list_filter = ('rating', 'create_time', 'author')
    search_fields = ('author', )
    actions = [nullfy_rating]


class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.get_fields()]

admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
