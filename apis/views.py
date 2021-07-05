from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
from app.models import Posts
from apis.serializers import PostSerializer

class PostList(APIView):

    def get(self,request,format=None):
        posts=Posts.objects.all()
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)



