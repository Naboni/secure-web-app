from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user.models import User
from captcha.fields import ReCaptchaField

class NewPasswordInput(forms.PasswordInput):
    def __init__(self, attrs=None):
        attrs = attrs or {}
        attrs['autocomplete'] = 'new-password'
        super().__init__(attrs)

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'autocomplete': 'off'}))
    password1 = forms.CharField(widget=NewPasswordInput)
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password1', 'password2', "captcha"]
        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password',
        }


class LoginForm(AuthenticationForm):
    captcha = ReCaptchaField()
