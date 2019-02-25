from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Форма комментариев"""
    class Meta:
        model = Comment
        fields = ("text", )
        widgets = {'text': forms.Textarea(attrs={"cols":80, "class": "form-control"})}