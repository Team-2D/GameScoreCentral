from django.db import models
from django.conf import settings
from category.models import GameCategory
from account.models import UserProfile

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_data = models.IntegerField()    #integer field as just using year
    poster = models.ImageField(upload_to='game_posters/')
    category = models.ForeignKey(GameCategory, on_delete=models.SET_NULL, null=True)
    game_studio = models.CharField(max_length=255)
    posted_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    average_review = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class GameReview(models.Model):
    rating = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(UserProfile, related_name='game_reviews', on_delete=models.CASCADE)
    game = models.ForeignKey('Game', related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.created_by.username} for {self.game.title}"
