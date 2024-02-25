from django.db import models
from django.contrib.auth.models import User

class avatar(models.Model):
    user = models.OneToOneField(User, blank=False, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="img/users/{user.username}", blank=True, null=True) 

    def __str__(self):
        return self.user.username
    