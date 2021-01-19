from django.urls import path 
from .views import stamp_list

app_name = 'stamp'


urlpatterns = [
    path('',stamp_list, name='stamp_list')
]
