from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .utils import validate_img_extension, validate_video_extension

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)  
    last_modified = models.DateTimeField(auto_now=True)  

    def clean(self) -> None:
        if self.file:
            if not validate_img_extension(self.file) and not validate_video_extension(self.file):
                raise ValidationError("El archivo debe ser una imagen o un video.")


    def save(self, *args, **kwargs):
        if not self.id:  
            self.created_on = timezone.now()  
        return super(Post, self).save(*args, **kwargs)
    def __str__(self):
        return self.title