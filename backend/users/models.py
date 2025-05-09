from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    old_cart = models.CharField(max_length=200, blank=True, null=True)
    premium = models.BooleanField(default=False)
    location_consent = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'