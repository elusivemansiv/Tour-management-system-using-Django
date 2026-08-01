from django.db import models

class BlogCategory(models.Model):
    name = models.CharField(max_length=50)
    color_class = models.CharField(max_length=50, default="bg-blue-600", help_text="Tailwind bg color class, e.g. bg-blue-600")

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "Blog Categories"

from ckeditor_uploader.fields import RichTextUploadingField

class BlogTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(BlogTag, blank=True, related_name='posts')
    
    # Author details
    author_name = models.CharField(max_length=100)
    author_role = models.CharField(max_length=100, default="Author")
    author_avatar = models.ImageField(upload_to='blog/authors/', blank=True, null=True)
    author_bio = models.TextField(blank=True, null=True, help_text="Short bio at the bottom of the article")
    author_facebook = models.URLField(blank=True, null=True)
    author_twitter = models.URLField(blank=True, null=True)
    author_linkedin = models.URLField(blank=True, null=True)
    
    date_posted = models.DateField(auto_now_add=True)
    read_time = models.PositiveIntegerField(default=5, help_text="Estimated read time in minutes")
    
    excerpt = models.TextField(help_text="Short description for the card")
    content = RichTextUploadingField(blank=True, null=True)
    
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    is_featured = models.BooleanField(default=False, help_text="Show in the large top-left spot")
    is_text_only = models.BooleanField(default=False, help_text="Design with gray background and no image")
    video_url = models.URLField(blank=True, null=True, help_text="If provided, shows a video play button overlay")

    def __str__(self):
        return self.title

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
