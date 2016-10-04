from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

import datetime

class Team(models.Model):
    """Team Model"""
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)

    primary_color = models.CharField(max_length=100, default="")
    secondary_color = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name

class Player(models.Model):
    """Player Model"""
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField('Date of Birth')
    position = models.CharField(max_length=100)
    number = models.PositiveIntegerField(default=0)
    hometown = models.CharField(max_length=200, default="Hometown")
    nationality = models.CharField(max_length=100, default="Nation")
    comment_count = models.PositiveIntegerField('Comment Count', default=0)

    def __str__(self):
        return self.name

class Comment(models.Model):
    """Comment Model"""
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    text = models.CharField(max_length=500)
    post_date = models.DateField('Created')

    def __str__(self):
        return self.text[:10]


class EndUser(models.Model):
    """End User Model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favourite_team = models.ForeignKey(Team)
    favourite_players = models.CharField(max_length=300, default="", blank=True)

    def __str__(self):
        return self.user.first_name
    
    
