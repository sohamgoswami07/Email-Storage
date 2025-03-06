from django import forms
from .models import Ratings

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Ratings
        fields = ['ratings']