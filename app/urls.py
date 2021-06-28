from django.urls import path
from .views import all_blogs, blog_detail
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", all_blogs, name="all_blogs"),
    path("<int:pk>/", blog_detail, name="blog_detail"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()