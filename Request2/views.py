
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Request2.models import requestCla, RequestType
from Shopping_cart.car import Car
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from Shopping_cart.views import cleanCar
#from store.Templates.emails

# Create your views here.

@login_required(login_url="/authentication/login")
def processRequest(request):
    requestVar= requestCla.objects.create(userVar= request.user)
    car = Car(request)
    requestLines= list()


    
    for key, value in car.car.items():
        requestLines.append(RequestType(
            producto_id=key,
            amount=value["amount"],
            userVar=request.user, 
            requestVar= requestVar
        ))
    print(requestLines)
    RequestType.objects.bulk_create(requestLines)

    sendMail(
        requestVar=requestVar,
        requestLines=requestLines, 
        nameUser= request.user.username, 
        userEmail=request.user.email

    )
    messages.success(request, "Your purchase was succesfully saved")
    cleanCar(request)
    
    return redirect('../store/shopcarurl/')

def sendMail(**kwargs):
    subject= "thanks for your purchase "
    messageMail= render_to_string("emails/request.html", {
        "requestVar": kwargs.get("requestVar"),
        "requestLines": kwargs.get("requestLines"),
        "nameUser": kwargs.get("nameUser")
    })

    text_message = strip_tags(messageMail)
    from_email="juansossa1468@gmail.com"
    to_email= kwargs.get("userEmail")
    #to_email= "cotizaciones@qualitascolombia.com"

    send_mail(subject, text_message, from_email, [to_email], html_message=messageMail )