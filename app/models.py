from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Posts(models.Model):

    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to="blog_images")
    post_on = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now_add=True)
    categories = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comments(models.Model):
    author = models.CharField(max_length=20)
    description = models.TextField()
    post_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.author
