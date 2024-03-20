from django.db import models
from django.conf import settings
from category.models import GameCategory

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=255) # 创建字符串
    description = models.TextField() # 字符串
    release_data = models.IntegerField() #整数
    poster = models.ImageField(upload_to='game_posters/') #路径 =》 字符串
    category = models.ForeignKey(GameCategory, on_delete=models.SET_NULL, null=True)# 外键 创建对应的类
    game_studio = models.CharField(max_length=255)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    average_review = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def avg_review(self):
        reviews = GameReview.objects.filter(game=self)
        if reviews:
            total_reviews = len(reviews)
            total_score = sum(review.rating for review in reviews)
            return round(total_score/total_reviews, 1)
        else:
            return 0

class GameReview(models.Model):
    rating = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='game_reviews', on_delete=models.SET_NULL, null=True, blank=True)
    game = models.ForeignKey('Game', related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.created_by.username} for {self.game.title}"
