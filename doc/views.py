from django.shortcuts import render
from django.core.mail import send_mail
from .models import Patient


def home(request):
    return render(request,'home.html',{})

def appointment(request):
    #database and assignment 
    if request.method == "POST":
        if request.POST.get('your-name') and request.POST.get('your-phone') and request.POST.get('your-email') and request.POST.get('your-day') and request.POST.get('your-scheldule'):
            post=Patient()
            post.name=request.POST.get('your-name')
            post.phone=request.POST.get('your-phone')
            post.email=request.POST.get('your-email')
            post.schedule=request.POST.get('your-scheldule')
            post.day=request.POST.get('your-day')
            post.Service=request.POST.get('your-Service')
            post.message=request.POST.get('your-message')
            post.save()
           
            your_name = request.POST['your-name']
            your_phone = request.POST['your-phone']
            your_email = request.POST['your-email']
            your_address = request.POST['your-address']
            your_scheldule = request.POST['your-scheldule']
            your_day = request.POST['your-day']
            your_Service=request.POST['your-Service']
            your_message = request.POST['your-message']

            #email
            appointment="Name:" + your_name + "\n  Phone:" + your_phone + "\n  Email:" + your_email + "\n  address:" + your_address + "\n  Schedule:" + your_scheldule + "\n  day:" + your_day + "\n Service:" + your_Service + "\n  Message:" + your_message

            send_mail(
                'Appointment Request',
                appointment,
                your_email,
            ['appoint4541@gmail.com']
            )
            send_mail(
                'Form submitted',
                'We will contact you on '+ your_phone +' shortly for time availability and token \n Thank you',
                'appoint4541@gmail.com',
                [your_email],
                fail_silently=False
            )
            
            return render(request,'appointment.html',{
                'your_scheldule':your_scheldule,
                'your_name':your_name,
                'your_phone': your_phone,
                'your_email':your_email,
                'your_address':your_address,
                'your_day':your_day,
                'your_Service':your_Service,
                'your_message': your_message,
                })
    else:
            return render(request,'home.html',{})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_phone = request.POST['message-phone']
        message = request.POST['message']
        
        #sending email
        send_mail(
            message_name,#subject
            message,#message
            message_email,#from email
            ['appoint4541@gmail.com'],#to email
        )
        send_mail(
                'We will get in touch with you shortly',
                'We will contact you shortly on ' + message_phone + ' for clearing your doubts \n Thank you',
                'appoint4541@gmail.com',
                [message_email],
                fail_silently=False
            )

        return render(request,'contact.html',{'message_name':message_name})
    else:
        return render(request,'contact.html',{})

def pricing(request):
    return render(request,'pricing.html',{})

def service(request):
    return render(request,'service.html',{})

