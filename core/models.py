from django.db import models
from django.contrib.auth.models import AbstractUser 

class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    organization = models.ForeignKey(Organization, related_name='roles', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class User(AbstractUser ):
    email = models.EmailField(unique=True)
    organization = models.ForeignKey(Organization, related_name='users', on_delete=models.CASCADE)
    roles = models.ManyToManyField(Role, related_name='users')

    def __str__(self):
        return self.username