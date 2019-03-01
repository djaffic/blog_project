from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Форма комментариев"""
    class Meta:
        model = Comment
        fields = ("text",)
        # exclude = ("post",)
        widgets = {
            'text': forms.Textarea(attrs={"class": "form-control", "placeholder": "Оставьте свой комментарий"})
        }