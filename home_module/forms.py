from django import forms
from django.core.validators import RegexValidator


class ContactForm(forms.Form):
    full_name = forms.CharField(
        min_length=6,
        max_length=128,
        widget=forms.TextInput(attrs={
            'placeholder': 'نام و نام خانوادگی',
            'class': 'form-control',
        })
    )

    phone = forms.CharField(
        min_length=11,
        max_length=11,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'تلفن همراه شما',
        }),
        validators=[
            RegexValidator(
                regex=r'^09\d{9}$',
                message='تلفن همراه خود را درست وارد کنید!'
            )
        ],
    )

    message = forms.CharField(
        min_length=10,
        max_length=5000,
        widget=forms.Textarea(attrs={
            'placeholder': 'متن پیام شما',
            'class': 'form-control',
        })
    )
