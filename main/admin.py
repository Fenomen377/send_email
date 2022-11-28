# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin import ModelAdmin

from main.models import Follower


@admin.register(Follower)
class FollowerAdmin(ModelAdmin):
    list_display = ('name', 'email')

