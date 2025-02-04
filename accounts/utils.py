from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_welcome_email(user):
    subject = 'Welcome to Our E-Commerce Site!'
    html_message = render_to_string('emails/welcome_email.html', {'user': user})
    plain_message = strip_tags(html_message)
    from_email = 'salah10saeed@gmail.com'
    to_email = user.email

    email = EmailMultiAlternatives(subject, plain_message, from_email, [to_email])
    email.attach_alternative(html_message, "text/html")
    email.send()
