# Django
from django import forms

# Models
from posts.models import Post


class PostForm(forms.ModelForm):
    """Formulario de post"""

    class Meta:
        """Form settings."""

        model = Post
        fields = ('user', 'profile', 'title', 'photo')

