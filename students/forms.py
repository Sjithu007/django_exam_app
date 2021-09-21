from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator

class SignUpForm(UserCreationForm):

    username_validation = RegexValidator(r'^[a-z]*$', 'Username must contain only lowercase alphabets.')

    username = forms.CharField(max_length=12, validators=[username_validation], widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-sm'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control form-control-sm'})) 

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-sm'
