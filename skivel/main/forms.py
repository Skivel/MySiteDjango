from django import forms
from .models import ContactMe


class PostContact(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = '__all__'