from django.urls import path, include

from game import views

app_name = 'game'

urlpatterns = [
    path('', views.viewAllGames, name='viewAllGames'),
    path('<int:id>/', views.viewGame, name='viewGame'),
    path('new/', views.addNewGame, name='addNewGame'),
    path('addreview', views.addReview, name='addReview'),
]
