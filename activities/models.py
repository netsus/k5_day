from django.conf import settings
from django.db import models

class Activity(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    photo=models.ImageField()
    liked_user_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="liked_activity_set"
    )
    participants = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

