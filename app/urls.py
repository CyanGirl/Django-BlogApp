from django.urls import path
from .views import all_blogs, blog_detail,edit_blog,add_blog,delete_blog,export_blog
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", all_blogs, name="all_blogs"),
    path("<int:pk>/", blog_detail, name="blog_detail"),
    path("blog/<int:pk>/",edit_blog,name="edit_blog"),
    path("new/",add_blog,name="add_blog"),
    path("delete/<int:pk>/",delete_blog,name="delete_blog"),
    path("download/<int:pk>/",export_blog,name="export"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()

