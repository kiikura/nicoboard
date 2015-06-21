# -*- coding: utf-8 -*-
from django.db import models

class Board(models.Model):
    name = models.SlugField(max_length=50, unique=True)
    owner = models.ForeignKey("auth.User", blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name;

class Message(models.Model):
    board = models.ForeignKey("Board")
    body = models.TextField(max_length=5000, blank=True)
    owner = models.ForeignKey("auth.User", blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
