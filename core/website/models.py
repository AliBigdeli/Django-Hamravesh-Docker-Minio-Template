from django.db import models

# Create your models here.

class Photo(models.Model):
    file = models.ImageField(upload_to="photos/")

    def __str__(self):
        return self.file.name