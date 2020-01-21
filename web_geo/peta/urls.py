from django.urls import path
from .views import HomePageView, point_datasets

app_name = 'peta'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('data/', point_datasets, name='data'),
]
