from django.core.mail import send_mail
from django.conf import settings

def send_email_email():
    subject = "This is from the Django server"
    message = "This is a test email, don't worry!"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["azharkhanzada356@gmail.com"]  # Fixed typo in the email address
    send_mail(subject, message, from_email, recipient_list)
