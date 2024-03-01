from django.urls import path, include

from account import views

app_name = 'account'

urlpatterns = [
    path('', views.profilePage, name='profile'),
    path('edit/', views.editProfile, name='editProfile'),
    path('view/<int:id>', views.viewProfile, name='viewProfile'),
]
