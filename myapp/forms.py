from django import forms
from .models import *

from.models import userdetails
class userform(forms.ModelForm):
    class Meta:
        model=userdetails
        fields='__all__'
# class academicform(forms.ModelForm):
#     class Meta:
#         model=academicdetails
#         fields='__all__'

class skillform(forms.ModelForm):
    class Meta:
        model=skill
        fields=['skill1','skill2','skill3']