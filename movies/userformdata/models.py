from django.db import models


class MovieBooking(models.Model):
    movie_choices = [
        ('Avengers: Endgame', 'Avengers: Endgame'),
        ('The Shawshank Redemption', 'The Shawshank Redemption'),
        ('The Godfather', 'The Godfather'),
        ('The Dark Knight', 'The Dark Knight'),
        ('Pulp Fiction', 'Pulp Fiction'),
    ]
    
    movie = models.CharField(max_length=100, choices=movie_choices)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    quantity = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

# Create your models here.
