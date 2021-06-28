from django.contrib import admin
from .models import Posts, Category, Comments

# Register your models here.
admin.site.register(Posts)
admin.site.register(Category)
admin.site.register(Comments)
