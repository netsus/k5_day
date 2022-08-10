from django.shortcuts import render
from django.views.generic import ListView, DetailView

from activities import models


class ActivityListView(ListView):

    """ Activity List View Definition"""

    model = models.Activity
    ordering = "id"
    context_object_name = "activities"


class ActivityDetailView(DetailView):
    model = models.Activity
