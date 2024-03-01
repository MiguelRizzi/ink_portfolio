from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)  
    last_modified = models.DateTimeField(auto_now=True)  

    def save(self, *args, **kwargs):
        if not self.id:  
            self.created_on = timezone.now()  
        return super(Post, self).save(*args, **kwargs)
    def __str__(self):
        return self.title