from django.contrib.auth import get_user_model
from django import forms

non_allowed_usernames = ['abc']

# check for unique username & email

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'user-password'
            }
        )
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'user-confirm-password'
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexcact=username) # thisIsMyUsername == thisismyusername

        if username in non_allowed_usernames:
            raise forms.ValidationError('This is an invalid username, please pick another')

        if not qs.exists():
            raise forms.ValidationError('This is an invalid username, please pick another')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email) # thisIsMyemail == thisismyemail
        if not qs.exists():
            raise forms.ValidationError('This email is already in use')
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'user-password'
            }
        )
    )

    # def clean(self): # last method called
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')


    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username) # thisIsMyUsername == thisismyusername
        if not qs.exists():
            raise forms.ValidationError('This is an invalid user')
        return username