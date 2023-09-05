from django import forms
from forum_app.models import Post, Tag


class PostForm(forms.models.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'tags']

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'choices'}),
    )
