# from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Image

User = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta:
        """Meta class"""
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone')


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        # fields = '__all__'
        fields = ('title', 'description', 'image')
        # labels = {'photo': ''}

# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ('title', 'description', 'image')
