from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('thanks')
    else:
        form = ContactForm()
        return render(request, 'contactform/contactform.html', {'form': form})


class ContactFormView(View):
    """отправка формы обратной связи"""
    def post(self, request):
        form = ContactForm(request.POST)
        # if request.user.is_authenticated:
        if form.is_valid():
            # form = form.save(commit=False)
            # form["first_name"] = form.cleaned_data['first_name']
            # form["last_name"] = form.cleaned_data['last_name']
            # form["father_name"] = form.cleaned_data['father_name']
            # form["email"] = form.cleaned_data['email']
            # form["content"] = form.cleaned_data['content']
            form.save()
            return render(request, 'contactform/thanks.html', {})
        else:
            form = form.ContactForm()
            return render(request, 'contactform/contactform.html', {'form': form})

