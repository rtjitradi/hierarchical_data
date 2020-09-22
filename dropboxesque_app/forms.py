from django import forms

from dropboxesque_app.models import DropboxesqueModel


class DropboxesqueForm(forms.ModelForm):
    class Meta:
        model = DropboxesqueModel
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
