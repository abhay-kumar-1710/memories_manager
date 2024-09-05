from django import forms
from myapp.models import ImageUploader
from django.contrib.auth.models import User 
from django.contrib.auth.forms import AuthenticationForm

class ImageUploaderForm(forms.ModelForm):
    class Meta:
        model = ImageUploader
        fields = ["title","date", "image"]
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'date' : forms.DateInput(attrs={'class' : 'form-control', 'id' :'datepicker', 'autocomplete': 'off'}),
        }

# LOG IN
class UserLogInForm(AuthenticationForm):
    username = forms.CharField(widget= forms.TextInput(attrs={"class": "form-control mt-1"}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={"class": "form-control mt-1"}))
    class Meta:
        model = User
        fields = ["username", "password"]