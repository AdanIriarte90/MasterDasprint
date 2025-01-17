#!/usr/bin/python

import smtplib, ssl
from django import forms

class Formulario (forms.Form):
    nombre=forms.CharField(max_length=100)
    mensaje=forms.CharField()
    mail=forms.EmailField()

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "my@gmail.com"
    password = forms.CharField(widget=forms.TextInput)

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        # TODO: Send email here
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()