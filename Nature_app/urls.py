from django.urls import path
from . import views

app_name = 'nature_app'

urlpatterns = [
    path('detail/', views.nature, name='nature')
]