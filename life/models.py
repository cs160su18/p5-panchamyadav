from django.db import models

class Group(models.Model):
	established = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
  
  
class User(models.Model):
  username = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  
class MiniGame(models.Model):
  name = models.CharField(max_length=50)

class Score(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  game = models.ForeignKey(MiniGame, on_delete=models.CASCADE)
  heart_rate = models.IntegerField()
  distance = models.FloatField()
  score = models.FloatField()
  