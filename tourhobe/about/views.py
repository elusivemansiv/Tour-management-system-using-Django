from django.shortcuts import render
from .models import AboutHero, AboutStory, AboutFeature, AboutTeamMember

def about(request):
    hero = AboutHero.objects.first()
    story = AboutStory.objects.first()
    features = AboutFeature.objects.all()
    team = AboutTeamMember.objects.all()
    
    return render(request, "about/about.html", {
        'hero': hero,
        'story': story,
        'features': features,
        'team': team,
    })
