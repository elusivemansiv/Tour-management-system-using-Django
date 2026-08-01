from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import SiteSetting

@admin.register(SiteSetting)
class SiteSettingAdmin(ModelAdmin):
    fieldsets = (
        ('General Settings', {
            'fields': ('site_name', 'logo', 'favicon')
        }),
        ('Contact Information', {
            'fields': ('contact_email', 'phone1', 'phone2', 'location_address', 'map_iframe_url'),
            'description': 'Contact information displayed on the contact page and footer.'
        }),
        ('Social Media Links', {
            'fields': ('facebook_url', 'instagram_url', 'twitter_url', 'linkedin_url'),
            'description': 'Links to social media profiles.'
        }),
        ('Developer Credits Configuration', {
            'fields': ('show_developer_credits', 'developer_credit_text'),
            'description': 'Configure whether to show developer credits in the footer.'
        }),
        ('First Developer / Company', {
            'fields': ('show_developer1', 'developer1_name', 'developer1_url'),
        }),
        ('Second Developer', {
            'fields': ('show_developer2', 'developer2_name', 'developer2_url'),
        }),
    )
