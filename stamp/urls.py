from django.urls import path 
from .views import stamp_list_filter

app_name = 'stamp'


urlpatterns = [
    path('',stamp_list_filter, name='stamp_list')
]
