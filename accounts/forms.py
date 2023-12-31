from django import forms
from django.contrib.auth.models import User


# Form to Edit Post
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
