from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from blog_project import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm


# def contact(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('thanks')
#     else:
#         form = ContactForm()
#         return render(request, 'contact/contact.html', {'form': form})


class ContactFormView(View):
    """отправка формы обратной связи"""
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact/contact.html', {"form": form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            print(name, email, subject, message)
            recipient_list = ['it@vniir.org']
            sender = settings.EMAIL_HOST_USER
            try:
                send_mail(subject, message, sender, recipient_list)
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
            form.save()
            messages.add_message(request, settings.MY_INFO, "Спасибо за обращение")

        else:
            messages.add_message(request, settings.MY_INFO, "Вы допустили ошибку при заполнении формы")
        return redirect('contact')

