from django.urls import path, include

from game import views

app_name = 'game'

urlpatterns = [
    path('', views.viewAllGames, name='viewAllGames'),
    path('<int:id>/', views.viewGame, name='viewGame'),
    path('new/', views.addNewGame, name='addNewGame'),
    path('addreview', views.addReview, name='addReview'),
    path('editReview/<int:review_id>/', views.editReview, name='editReview'),
    path('deletereview/<int:review_id>/', views.deleteReview, name='deleteReview'),
    path('search/', views.searchGames, name='searchGames'),
]
