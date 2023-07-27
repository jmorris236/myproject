# behavior_app/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Behavior(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Note(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='notes')
    behavior = models.ForeignKey(Behavior, on_delete=models.CASCADE)
    note = models.TextField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.student}: {self.behavior} - {self.date}"
