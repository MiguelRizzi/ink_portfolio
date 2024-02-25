from django.db import models


class Tattoo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='img/tattoos')
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Design(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='img/designs')
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - available ={self.available}"