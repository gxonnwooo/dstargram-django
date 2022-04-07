from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Photo(models.Model):
    objects = None
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_photos")
    photo = models.ImageField(blank=True, null=True)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('photo: photo_detail', args=[str(self.id)])