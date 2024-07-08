from django import forms
from django.forms import ModelForm

from .models import AccType


class AccountTypeForm(ModelForm):
    accTypeName = forms.CharField(label='Account Type',widget= forms.TextInput(attrs={'class': 'form-control'}))
    #password = forms.CharField(label='Password',widget= forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = AccType
        fields = ['accTypeName']

