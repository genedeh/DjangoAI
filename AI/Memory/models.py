from django.db import models
from uuid import uuid4


# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=20)
    code = models.UUIDField(primary_key=True, default=uuid4())
    image = models.ImageField()
    description = models.TextField(blank=True)
    email = models.EmailField(unique=True, blank=True)
    phone_number = models.IntegerField(unique=True, blank=True)
    group = models.ManyToManyField(to=Group, related_name="Person-Group")

    def __str__(self):
        return self.name

