from django import forms

from activities.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=[
            "content",
        ]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 2})
        }