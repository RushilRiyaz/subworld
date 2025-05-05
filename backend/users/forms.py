from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    premium = forms.BooleanField(
        required=False, help_text='Get 10% off on all purchases!')
    location_consent = forms.BooleanField(required=False)


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            profile = user.profile
            profile.premium = self.cleaned_data.get('premium', False)
            profile.location_consent = self.cleaned_data.get('location_consent', False)
            profile.save()
        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'premium', 'location_consent']
