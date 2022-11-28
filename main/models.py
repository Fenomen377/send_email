# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Follower(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name
