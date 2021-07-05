from django.urls import path
from apis.views import PostList

app_name="apis"

urlpatterns=[
    path("",PostList.as_view(),name="post_api"),
]

