from django.conf import settings
from django.db import models
from django.db.models import ForeignKey, OneToOneField

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
    master=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
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

class Registration(models.Model):
    user_regist=OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity_regist=ForeignKey("Activity", on_delete=models.CASCADE, related_name="registrations", blank=True, null=True)

    def __str__(self):
        return f"{self.activity_regist} - {self.user_regist}"

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity = models.ForeignKey("Activity", on_delete=models.CASCADE)
    content = models.TextField()
    like = models.PositiveIntegerField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

