

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import  Profile



class RegisterForm(forms.Form) :

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام کاربری' , 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'ایمیل کاربری' , 'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور '  , 'class' : 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'تایید رمز عبور '  , 'class' : 'form-control'}))



    def clean_username(self):
        my_username = self.cleaned_data['username']

        user = User.objects.filter(username=my_username).exists()



        if user :
            raise ValidationError("قبلا انتخاب شده است ")

        return my_username


    def clean_email(self):
        my_email = self.cleaned_data['email']

        user = User.objects.filter(email=my_email).exists()

        user = None
        if user :
            raise ValidationError("این ایمیل قبلا انتخاب شده است ")

        return my_email #
        #


class Loginform(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'نام کاربری' , 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs = {'placeholder' : 'رمز عبور ' , 'class' : 'form-control'}))



class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [  'first_name' , 'last_name' , 'bio' ]

