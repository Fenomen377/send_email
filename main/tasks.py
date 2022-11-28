# coding=utf-8
from django.core.mail import send_mail
from django.template import loader

from send_email.celerys import app

from .service import send
from .models import Follower


@app.task
def send_message_email(user_email):
    send(user_email)


@app.task
def send_beat_email():
    for follower in Follower.objects.all():
        send_mail(
            'Спасибо за подписку',
            '',
            'gkf5051@gmail.com',
            [follower.email],
            fail_silently=False,
            html_message=loader.render_to_string(
                'main/mail.html',
                {
                    'user_email': follower.name,
                    'subject': 'Благодарим вас за подписку и дарим вам промокод со скидкой 90% на всю нашу продукцию',
                }
            )
        )
