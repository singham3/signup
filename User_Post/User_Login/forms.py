from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class SignUpForm(forms.ModelForm):
    username = forms.CharField(required = True)
    full_name = forms.CharField(required = True)
    email = forms.EmailField(required = True)
    password = forms.CharField(widget=forms.PasswordInput)
    conform_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','full_name','email','password')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.full_name = self.cleaned_data['full_name']
        user.email = self.cleaned_data['email']
        user.password = self.cleaned_data['password']
        user.conform_password = self.cleaned_data['conform_password']

        if commit:
            user.save()

        return user

