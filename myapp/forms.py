from django import forms
from .models import User


# class UserForm(forms.Form):
#     name = forms.CharField(max_length=200)
#     password = forms.CharField(required=False)
#     roll = forms.IntegerField(min_value=0, initial=0)
#     email = forms.EmailField()
#     address = forms.CharField(widget=forms.Textarea, required=False)
   


class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields = '__all__'
        
   
  
   
