from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    """ Custom User Model """
    MALE = "male"
    FEMALE = "female"
    CHOICES = (
        (MALE, _("Male")),
        (FEMALE, _("Female")),
    )
    birthdate = models.DateField(_("birthdate"), blank=True, null=True)
    activity_master = models.BooleanField(default=False)
    participated_activity = models.ForeignKey(
        "activities.Activity", related_name="activities", null=True, on_delete=models.DO_NOTHING
    )

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})