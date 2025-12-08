from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import ContactForm
from .models import Contact


class HomeView(TemplateView):
    template_name = 'home_module/index.html'

    def get(self, request):
        contact_form = ContactForm()
        context = {
            'contact_form': contact_form
        }
        return render(request, 'home_module/index.html', context)

    def post(self, request):
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            new_form = Contact(
                user_full_name=contact_form.cleaned_data.get('full_name'),
                user_phone=contact_form.cleaned_data.get('phone'),
                user_message=contact_form.cleaned_data.get('message')
            )
            new_form.save()
            messages.success(request, 'پیام شما با موفقیت ثبت شد و طی 24 ساعت با شما تماس گرفته خواهد شد')
            return redirect('home')
        context = {
            'contact_form': contact_form
        }
        return render(request, 'home_module/index.html', context)
