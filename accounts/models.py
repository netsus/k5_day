from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    """ Custom User Model """
    MALE = "male"
    FEMALE = "female"
    GENDER_CHOICES = (
        (MALE, _("Male")),
        (FEMALE, _("Female")),
    )
    gender = models.CharField(
        _("gender"), choices=GENDER_CHOICES, max_length=10, blank=True
    )
    birthdate = models.DateField(_("birthdate"), blank=True, null=True)
    participated_activity = models.ForeignKey(
        "activities.Activity", related_name="activities", null=True,blank=True, on_delete=models.DO_NOTHING
    )

    def get_absolute_url(self):
        return reverse("accounts:profile")