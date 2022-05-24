from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    released_date = models.DateField()
    popularity = models.FloatField()
    vote_avg = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)
    win_worldcup = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='best_movies')
    movie_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='movie_like_user')
    
    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    content = models.TextField()

    def __str__(self):
        return self.content