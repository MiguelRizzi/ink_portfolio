from django.db import models


class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 - Malo'),
        (2, '2 - Regular'),
        (3, '3 - Promedio'),
        (4, '4 - Bueno'),
        (5, '5 - Excelente'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    review = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    aproved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    