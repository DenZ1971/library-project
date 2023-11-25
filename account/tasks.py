from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_welcome_email(user_email):
    subject = 'Welcome to our site'
    message = 'Thank you for your registartion'
    from_email = 'site@example.com'
    to_email = [user_email]
    send_mail(subject, message, from_email, to_email)