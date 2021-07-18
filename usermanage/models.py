from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="profile_images")
    bio = models.CharField(max_length=100)

    def __str__(self):
        return str(self.picture)
