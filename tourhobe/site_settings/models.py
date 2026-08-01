from django.db import models

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, default="Tour Hobe")
    logo = models.ImageField(upload_to='site_settings/', blank=True, null=True)
    favicon = models.ImageField(upload_to='site_settings/', blank=True, null=True)
    show_developer_credits = models.BooleanField(default=True, help_text="Show developer credits in the footer")
    
    # Developer credits fields
    developer_credit_text = models.CharField(max_length=200, default="developed by", help_text="Text before the developer names")
    
    show_developer1 = models.BooleanField(default=True, help_text="Show the first developer in the footer")
    developer1_name = models.CharField(max_length=100, default="Stradigtech", help_text="First developer/company name")
    developer1_url = models.URLField(default="https://stradigtech.com/", blank=True, help_text="First developer URL")
    
    show_developer2 = models.BooleanField(default=True, help_text="Show the second developer in the footer")
    developer2_name = models.CharField(max_length=100, default="Mansib", help_text="Second developer name")
    developer2_url = models.URLField(default="https://mansibahsan.netlify.app/", blank=True, help_text="Second developer URL")
    
    # Contact Info Fields
    contact_email = models.EmailField(default="example@gmail.com")
    phone1 = models.CharField(max_length=20, default="+1 23 456 789")
    phone2 = models.CharField(max_length=20, default="+(222)4567 589", blank=True)
    location_address = models.TextField(default="9th Ave, New York, NY, USA", blank=True)
    map_iframe_url = models.TextField(default="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3022.617354157121!2d-74.00164672346765!3d40.7484444353805!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c259ba8b8f2d57%3A0xcb1b68923d8c11aa!2s9th%20Ave%2C%20New%20York%2C%20NY%2C%20USA!5e0!3m2!1sen!2s!4v1700000000000!5m2!1sen!2s", blank=True)
    
    # Social Media
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    def __str__(self):
        return "Site Settings"
