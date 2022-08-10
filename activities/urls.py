from django.urls import path

from activities import views

app_name="activities"

urlpatterns = [
    path("", views.ActivityListView.as_view(), name="list"),
    path("<int:pk>", views.ActivityDetailView.as_view(), name="detail"),
]