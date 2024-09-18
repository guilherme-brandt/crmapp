from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator
from .models import Record

class SignUpForm(UserCreationForm):
    
    email = forms.EmailField(label = "", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    first_name = forms.CharField(label = "", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name'}))
    last_name = forms.CharField(label = "", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'   
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class AddRecord(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First name", "class": "form-control"}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last name", "class": "form-control"}))
    address = forms.CharField(max_length=100, required=True, widget=forms.widgets.TextInput(attrs={"id":"address", "placeholder":"Address", "class": "form-control"}))
    city = forms.CharField(max_length=50, required=True, widget=forms.widgets.TextInput(attrs={"id":"city", "placeholder":"City", "class": "form-control"}))
    state = forms.CharField(max_length=50, required=True, widget=forms.widgets.TextInput(attrs={"id":"state", "placeholder":"State", "class": "form-control"}))
    phone = forms.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\(\d{2}\) \d{4,5}-\d{4}$', message="Telefone inválido. Formato esperado: (XX) XXXXX-XXXX")],
        widget=forms.TextInput(attrs={"id": "phone", "placeholder":"Phone", "class": "form-control"})
    )
    zipcode = forms.CharField(
        max_length=9,
        validators=[RegexValidator(regex=r'^\d{5}-\d{3}$', message="CEP inválido. Formato esperado: XXXXX-XXX")],
        widget=forms.TextInput(attrs={"id": "zipcode", "placeholder":"Zipcode", "class": "form-control"})
    )
    class Meta:
        model = Record
        exclude = ('user',)
        

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
