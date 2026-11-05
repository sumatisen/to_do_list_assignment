"""
URL configuration for to_do_list_project.
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('to_do_list_app.urls')),
]

urlpatterns += staticfiles_urlpatterns()
