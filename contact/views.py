from django.shortcuts import render, redirect
from .forms import form
from django.core.mail import send_mail

# Create your views here.



def Contact(request):
    contactForm = form()

    if request.method =='POST':
        contactForm = form(data=request.POST)
        if contactForm.is_valid():
            name=request.POST.get("name")
            email= request.POST.get("email")
            content= request.POST.get("content")
            listMail=  ["juansossa1468@gmail.com", email]

            send_mail(name, content, email, listMail, fail_silently=False)

            return redirect("/contact/?valid")

    return render(request, 'Contact/contact.html', {'myContactForm': contactForm})
