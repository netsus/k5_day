from django.conf import settings
from django.db import models

class Photo(models.Model):
    """ Photo Model Definition """

    caption = models.CharField(max_length=100)
    file = models.ImageField(upload_to="activity_photos")
    activity = models.ForeignKey("Activity", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

class Activity(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    liked_user_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="liked_activity_set"
    )

    class Meta:
        verbose_name_plural = "Activities"

    def __str__(self):
        return self.title

    def first_photo(self):
        try:
            (photo,) = self.photo_set.all()[:1]
            print(photo)
            return photo.file.url
        except ValueError:
            return None

    def get_all_photos(self):
        photos = self.photo_set.all()
        return photos

