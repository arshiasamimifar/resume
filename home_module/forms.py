from django import forms
from django.core.validators import RegexValidator


class ContactForm(forms.Form):
    full_name = forms.CharField(
        min_length=6,
        max_length=128,
        widget=forms.TextInput(attrs={
            'placeholder': 'نام و نام خانوادگی',
            'class': 'form-control',
        }),
        error_messages={
            'required': 'لطفاً نام و نام خانوادگی خود را وارد کنید.',
            'min_length': 'نام و نام خانوادگی باید حداقل ۶ کاراکتر باشد.',
            'max_length': 'طول نام و نام خانوادگی بیش از حد مجاز است.',
        }
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
                message='شماره تلفن همراه معتبر نیست. لطفاً با فرمت صحیح وارد کنید (مثال: 09123456789).'
            )
        ],
        error_messages={
            'required': 'لطفاً شماره تلفن همراه خود را وارد کنید.',
            'min_length': 'شماره تلفن همراه باید دقیقاً ۱۱ رقم باشد.',
            'max_length': 'شماره تلفن همراه باید دقیقاً ۱۱ رقم باشد.',
        }
    )

    message = forms.CharField(
        min_length=10,
        max_length=5000,
        widget=forms.Textarea(attrs={
            'placeholder': 'متن پیام شما',
            'class': 'form-control',
        }),
        error_messages={
            'required': 'لطفاً متن پیام را وارد کنید.',
            'min_length': 'متن پیام خیلی کوتاه است. لطفاً توضیحات بیشتری بنویسید.',
            'max_length': 'متن پیام بیش از حد طولانی است. لطفاً پیام را کوتاه‌تر کنید.',
        }
    )
