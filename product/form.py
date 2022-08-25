from django import forms

from .models import Product
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UploadProduct(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Product Name'}),
            'intro': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Product Intro'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
            'specification': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Specification'}),
            'category': forms.Select(attrs={'class':'form-control', 'placeholder':'Category'}),
            'color': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Color'}),
            'price': forms.NumberInput(),
            'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'}),
            'stock': forms.NumberInput()
        }

class UserForm(UserChangeForm):

    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'firstname':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'lastname':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'})
        } 
        
