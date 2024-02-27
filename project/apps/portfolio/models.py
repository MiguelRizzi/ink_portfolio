from django.db import models


class Tattoo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='img/tattoos')

    def __str__(self):
        return self.title

class Design(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='img/designs')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateField(auto_now=True)
    is_read = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name