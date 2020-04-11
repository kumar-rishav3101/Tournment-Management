from django.db import models
from django.urls import reverse

# Create your models here.
class Tournment(models.Model):
    name = models.CharField(max_length=264)
    def __str__(self):
        return self.name

class Teams(models.Model):
    tourn_id=models.ForeignKey(Tournment,related_name='teams',on_delete=models.CASCADE)
    name = models.CharField(max_length=264)
    owner = models.CharField(max_length=264)
    def __str__(self):
        return self.name


class Player(models.Model):
    team_id=models.ForeignKey(Teams,related_name='player',on_delete=models.CASCADE)
    tourn_id=models.ForeignKey(Tournment,related_name='player',on_delete=models.CASCADE)
    name = models.CharField(max_length=264)
    skill = models.CharField(max_length=264)
    runs = models.IntegerField(max_length=264)
    wickets = models.IntegerField(max_length=264)
    def __str__(self):
        return self.name
