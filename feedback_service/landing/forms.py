from django import forms



class LoginForm(forms.Form):
    logusername = forms.CharField(label="Enter your username", max_length=10, required=True)
    logpassword = forms.CharField(label="Enter your password", max_length=10, required=True)


class RegisterForm(forms.Form):
    username = forms.CharField(label="Enter your username", max_length=100, required=True)
    email = forms.CharField(label="Enter your email", max_length=100, required=True)
    password = forms.CharField(label="Enter your password", max_length=100, required=True)
    confirmpassword = forms.CharField(label="Confirm your password:", max_length=100, required=True)

