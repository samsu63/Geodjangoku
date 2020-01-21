from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('peta.urls', namespace='peta')),
    path('admin/', admin.site.urls),
]
