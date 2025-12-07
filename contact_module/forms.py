from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(
        min_length=6,
        max_length=128,
        widget=forms.TextInput(attrs={
            'placeholder': 'نام و نام خانوادگی',
            'class': 'form-control',
        })
    )


    phone = forms.EmailField(
        min_length=5,
        max_length=255,
        widget=forms.EmailInput(attrs={
            'placeholder': 'تلفن همراه',
            'class': 'form-control',
        })
    )

