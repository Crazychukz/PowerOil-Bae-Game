__author__ = 'CrazychukZ'
from django import forms

class RequestInviteForm(forms.Form):
    ans01 = forms.CharField(required=True)
    ans02 = forms.CharField(required=True)
    ans03 = forms.CharField(required=True)