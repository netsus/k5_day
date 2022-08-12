from django.contrib import admin
from django.utils.safestring import mark_safe

from activities import models

class PhotoInline(admin.TabularInline):

    model = models.Photo

@admin.register(models.Activity)
class ActivityAdmin(admin.ModelAdmin):

    """ Activity Admin Definition """

    inlines = (PhotoInline,)

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f"<img width='150px' src='{obj.file.url}' />")

    get_thumbnail.short_description = "Thumbnail"

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):

    """ Comment Admin Definition """
    pass

@admin.register(models.Registration)
class RegistrationAdmin(admin.ModelAdmin):

    """ Registration Admin Definition"""
    pass