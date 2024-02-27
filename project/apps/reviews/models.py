from django.db import models


class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 - Malo'),
        (2, '2 - Regular'),
        (3, '3 - Promedio'),
        (4, '4 - Bueno'),
        (5, '5 - Excelente'),
    ]
    name = models.TextField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    