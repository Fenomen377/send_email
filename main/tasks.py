from django.core.mail import send_mail
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
            'Hello',
            "Good morning",
            'gkf5051@gmail.com',
            [follower.email],
            fail_silently=False,
        )
