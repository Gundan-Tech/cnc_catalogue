from django.contrib import admin
from django.urls import path, include
from django.conf import settings             # <-- Add this
from django.conf.urls.static import static   # <-- Add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalogue.urls')),
]

# This tells the server how to find your images while you are building the site
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)