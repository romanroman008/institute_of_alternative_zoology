from django.forms import forms

from myapp.models import Curiosity


class CuriosityForm(forms.Form):
    class Meta:
        model = Curiosity
        fields = ['topic', 'content', 'stupidity_scale']