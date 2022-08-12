import json
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from activities.forms import CommentForm
from activities.models import Comment, Activity, Registration


class ActivityListView(ListView):

    """ Activity List View Definition"""

    model = Activity
    ordering = "id"
    context_object_name = "activities"

    def get(self, request, *args, **kwargs):
        activities_qs = self.get_queryset()
        regists_qs = [Registration.objects.filter(activity_regist_id=activity.pk).count() for activity in activities_qs]
        activities_regists = zip(activities_qs,regists_qs)
        return render(request, "activities/activity_list.html", {'activities_regists': activities_regists})



class ActivityDetailView(DetailView):

    """ Activity Detail View Definition """

    model = Activity

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        activity_pk = self.kwargs['pk']
        current_regist = Registration.objects.filter(user_regist_id=self.request.user.id)
        qs = Registration.objects.filter(activity_regist_id=activity_pk)
        context_data["registration_count"] = qs.count()
        context_data["registration_user_id_set"] = [i.user_regist_id for i in qs]
        context_data["current_regist"] = bool(current_regist)
        context_data["comment_form"] = CommentForm()
        return context_data

@login_required
def regist(request, activity_pk):
    user_id = request.user.id
    Registration.objects.create(
        user_regist_id=user_id,
        activity_regist_id=activity_pk
    )
    return redirect(resolve_url("activities:detail", activity_pk))

def user_check(user):
    return user.pk == user.registration.user_regist_id

@user_passes_test(user_check)
def delete_regist(request, activity_pk):
    Registration.objects.filter(
        user_regist_id=request.user.id,
        activity_regist_id=activity_pk,).delete()
    print('>>>>>>>>',Registration.objects.all())
    return redirect(resolve_url("activities:detail", activity_pk))




class CommentCreateView(LoginRequiredMixin, CreateView):

    """ Comment Create View Definition """

    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.activity = get_object_or_404(Activity, pk=self.kwargs["activity_pk"])
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return resolve_url("activities:detail", self.kwargs["activity_pk"])
        # return reverse("activities:detail", kwargs={'pk': self.kwargs["activity_pk"]})

class CommentUpdateView(UserPassesTestMixin, UpdateView):

    """ Comment Update View Definition """

    model = Comment
    form_class = CommentForm
    template_name = "form.html"

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return resolve_url("activities:detail", self.kwargs["activity_pk"])

class CommentDeleteView(UserPassesTestMixin, DeleteView):

    """ Comment Delete View Definition """

    model = Comment

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return resolve_url("activities:detail", self.kwargs["activity_pk"])

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
@login_required()
def likes(request, activity_pk):
    if is_ajax(request):
        activity = Activity.objects.get(id=activity_pk)
        user = request.user
        if activity.liked_user_set.filter(id = user.id).exists():
            activity.liked_user_set.remove(user)
            message="notgood"
        else:
            activity.liked_user_set.add(user)
            message="good"
        context={'like_count':activity.liked_user_set.count(),
                 'message':message}
        return HttpResponse(json.dumps(context), content_type="application/json")