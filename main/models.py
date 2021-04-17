
from __future__ import unicode_literals
from datetime import datetime, timedelta, timezone
from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    STATUS = [("new", "New"),
              ("inprogress", "In Progress"),
              ("closed", "Closed")]

    def ten_minutes_hence():
        return datetime.now() + timedelta(minutes=30)

    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    deadline = models.DateTimeField(default=ten_minutes_hence)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, default=None)
    status = models.CharField(max_length=10, choices=STATUS, default="new")

    def __str__(self):
        return self.title
