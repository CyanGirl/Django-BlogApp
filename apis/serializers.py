from django.db.models import fields
from rest_framework import serializers
from app.models import Posts


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model=Posts
        fields=['title','body','post_on']

        