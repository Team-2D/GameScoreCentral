from django.urls import path, include

from account import views

app_name = 'account'

urlpatterns = [
    path('profile/', views.profilePage, name='profile'),
    path('edit/', views.editProfile, name='editProfile'),
    path('view/<str:username>', views.viewProfile, name='viewProfile'),
    path('logout/', views.user_logout, name='logout')
]
