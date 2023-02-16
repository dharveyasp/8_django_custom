from django import forms
from .models import User

non_allowed_usernames = ['abc']


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', ]

    username = forms.CharField(strip=False)
    email = forms.EmailField()
    password1 = forms.CharField(
        strip=False,
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                "id": "user-password"
            }
        )
    )
    password2 = forms.CharField(
        strip=False,
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                "id": "user-confirm-password"
            }
        )
    )

    # Check if passwords match
    def check_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise forms.ValidationError("Please retype your password")
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    # Checks if inputted username matches existing User
    def check_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if username in non_allowed_usernames:
            raise forms.ValidationError("Invalid Username, please use another.")
        if qs.exists():
            raise forms.ValidationError("This username is already in use.")
        return username

    # Check if email is already in use
    def check_email(self):
        email = self.cleaned_data.get("username")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already in use.")
        return email


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )

    def check_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)  # gets inputted username and then checks if exists
        if not qs.exists():
            raise forms.ValidationError("This is an invalid user.")
        if qs.count() != 1:
            raise forms.ValidationError("This is an invalid user.")
        return username
