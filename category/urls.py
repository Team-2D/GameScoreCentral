from django.urls import path, include

from category import views

app_name = 'category'

urlpatterns = [
    path('', views.home, name='home'),
]
