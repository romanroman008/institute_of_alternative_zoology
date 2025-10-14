

from myapp.models import Curiosity, Comment
from django import forms

class CuriosityForm(forms.Form):
    class Meta:
        model = Curiosity
        fields = ['topic', 'content', 'stupidity_scale']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                "placeholder": "maksymalnie 500 znaków",
                "rows": 10,
                "cols": 50,
                "maxlength":500,
                "class": "text-center font-semibold"
            })
        }