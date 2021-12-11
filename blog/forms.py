# project/blog/forms.py

from django import forms
from .models import Blog

from markdownx.widgets import MarkdownxWidget


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'text')
        widgets = {
                'text': MarkdownxWidget(),
        }
