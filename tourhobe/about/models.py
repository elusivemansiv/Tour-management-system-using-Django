from django.db import models

class AboutHero(models.Model):
    title = models.CharField(max_length=200, default="If You Want To See The World We Will Help You")
    description = models.TextField(default="Passage its ten led hearted removal cordial...")
    stat1_icon = models.CharField(max_length=50, default="🚀")
    stat1_text = models.CharField(max_length=100, default="14K+ Global Customers")
    stat2_icon = models.CharField(max_length=50, default="👑")
    stat2_text = models.CharField(max_length=100, default="10K+ Happy Customers")
    stat3_icon = models.CharField(max_length=50, default="🎯")
    stat3_text = models.CharField(max_length=100, default="1M+ Subscribers")
    main_image = models.ImageField(upload_to='about/', blank=True, null=True)
    top_right_image = models.ImageField(upload_to='about/', blank=True, null=True)
    bottom_right_image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return "About Hero Section"

class AboutStory(models.Model):
    title = models.CharField(max_length=200, default="Our Story")
    paragraph1 = models.TextField()
    paragraph2 = models.TextField()

    def __str__(self):
        return "About Story Section"
        
    class Meta:
        verbose_name_plural = "About Stories"

class AboutFeature(models.Model):
    title = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=50, help_text="e.g. fa-solid fa-hotel")
    color_class = models.CharField(max_length=50, help_text="e.g. orange")
    description = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

class AboutTeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about/team/', blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
