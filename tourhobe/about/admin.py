from django.contrib import admin
from .models import AboutHero, AboutStory, AboutFeature, AboutTeamMember
from unfold.admin import ModelAdmin

@admin.register(AboutHero)
class AboutHeroAdmin(ModelAdmin):
    pass

@admin.register(AboutStory)
class AboutStoryAdmin(ModelAdmin):
    pass

@admin.register(AboutFeature)
class AboutFeatureAdmin(ModelAdmin):
    pass

@admin.register(AboutTeamMember)
class AboutTeamMemberAdmin(ModelAdmin):
    pass
