from django.urls import path

from activities import views

app_name="activities"

urlpatterns = [
    path("", views.ActivityListView.as_view(), name="list"),
    path("<int:pk>/", views.ActivityDetailView.as_view(), name="detail"),
    path("<int:activity_pk>/comment/new", views.CommentCreateView.as_view(), name="comment_new"),
    path("<int:activity_pk>/comment/<int:pk>/edit", views.CommentUpdateView.as_view(), name="comment_edit"),
    path("<int:activity_pk>/comment/<int:pk>/delete", views.CommentDeleteView.as_view(), name="comment_delete"),
    path("<int:activity_pk>/regist/", views.regist, name="regist"),
    path("<int:activity_pk>/regist/delete", views.delete_regist, name="delete_regist"),
    path("<int:activity_pk>/likes/", views.likes, name="likes"),
]