from django.template import loader,context
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core import mail
from django.core.mail import send_mail
from django.conf import settings
import smtplib, ssl
#from django.shortcuts import render_to_response,get_object_or_404
#from Functionalities.HomeApp.contacto import Formulario

# Create your views here.
def home(request):
    return render(request,'HomeApp/home.html')

def whoWeAre(request):
    return render(request,'HomeApp/nosotros.html')

def contact(request):    
    return render(request,'HomeApp/contacto.html')

def products(request):
    return render(request, 'HomeApp/productos.html')

def resultForm(request):
    #mensaje="formulario: %r" %request.POST["nombre"]
    #result=False

    nombre = request.POST["nombre"]
    mensaje = request.POST["mensaje"]
    mail = request.POST["email"]
    telefono = request.POST["telefono"]
    context = {}

    try:
        if request.method=='POST':
            subject = 'Mensaje de DASPrint.com.mx' 
            #message = 'HTML MENSAJE PRUEBA Python'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['adan.iriarte@gmail.com']

            message_body_mail='De ' + nombre + ',\r\n' + mensaje + '\r\n' + 'Email:' + mail + ', Telefono:' + telefono

            if send_mail(subject, message_body_mail, from_email, recipient_list, fail_silently=False,):
                context["email_response"] = "¡Correo enviado! Nos pondremos en contacto en menos de una hora."
                #return HttpResponse('Correo enviado')
                return render(request, 'HomeApp/contacto.html', context)
            else:
                context["email_response"] = "Hubo un error, intenta nuevamente por favor"
                #return HttpResponse('Correo enviado')
                return render(request, 'HomeApp/contacto.html', context)

        else:
            #return render(request,'HomeApp/contacto.html')
            return render(request, 'HomeApp/home.html', context)

    except:
        context["email_response"] = "El correo no se pudo enviar, intenta de nuevo."
        return render(request, 'HomeApp/contacto.html', context)


