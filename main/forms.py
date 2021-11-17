from django import forms
from .models import ContactProfile


class ContactForm(forms.ModelForm):

    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Nome Completo..',
            'class': 'form-control'
        }))

    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Email..',
            'class': 'form-control'
        })
    )

    message = forms.CharField(
        max_length=1000,
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': '*Mensagem..',
            'rows': 6
        })
    )

    class Meta:
        model = ContactProfile
        fields = ('name', 'email', 'message')