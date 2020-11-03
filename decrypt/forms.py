from django import forms
from .models import Snippet


class snippetforms(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = "__all__"
