# coding=utf-8
from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Hello',
        "Hi",
        'gkf5051@gmail.com',
        [user_email],
        fail_silently=False,
    )
