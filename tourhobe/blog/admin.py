from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import BlogCategory, BlogPost, NewsletterSubscriber, BlogTag

@admin.register(BlogPost)
class BlogPostAdmin(ModelAdmin):
    list_display = ('title', 'category', 'author_name', 'date_posted', 'is_featured')
    list_filter = ('category', 'is_featured', 'tags')
    search_fields = ('title', 'author_name')
    
    fieldsets = (
        ('General Information', {
            'fields': ('title', 'category', 'tags', 'image', 'video_url', 'is_featured', 'is_text_only', 'read_time')
        }),
        ('Author Information', {
            'fields': ('author_name', 'author_role', 'author_avatar', 'author_bio', 'author_facebook', 'author_twitter', 'author_linkedin')
        }),
        ('Content', {
            'fields': ('excerpt', 'content')
        }),
    )

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(ModelAdmin):
    list_display = ('email', 'subscribed_at')

@admin.register(BlogCategory)
class BlogCategoryAdmin(ModelAdmin):
    pass

@admin.register(BlogTag)
class BlogTagAdmin(ModelAdmin):
    pass
