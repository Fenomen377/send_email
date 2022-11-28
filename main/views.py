# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView

from main.forms import FollowerForm
from main.models import Follower
from main.service import send
from .tasks import send_message_email


class FollowerView(CreateView):
    model = Follower
    form_class = FollowerForm
    success_url = '/'
    template_name = 'main/follower.html'

    def form_valid(self, form):
        form.save()
        # send(form.instance.email)
        send_message_email.delay(form.instance.email)
        return super(FollowerView, self).form_valid(form)

