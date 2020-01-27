from django import forms
from django.forms.widgets import TextInput
from .models import Membership, Message


class JoinForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ('house',)
