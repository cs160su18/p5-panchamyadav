from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from life.models import *



def index(request):
    return render(request, 'life/login.html')
  
def main(request):
    return render(request, 'life/main.html')
  
def game(request):
    roomid = request.GET['roomid']
    game = MiniGame.objects.filter(name=roomid)
    
    if not game:
      new_game = MiniGame(name=roomid)
      new_game.save()
      game = MiniGame.objects.filter(name=roomid)
    
    request.session['roomid'] = roomid
    scores = Score.objects.filter(game=game[0]).values()
    scores_template = [{'username': User.objects.get(id = score['user_id']).username, 'heart_rate': score['heart_rate'],'distance': score['distance'], 'score': score['score']} for score in scores]
    scores_template = sorted(scores_template, key=lambda x: x['score'], reverse=True)
    return render(request, 'life/game.html', {"username": request.session['username'], "roomid": request.session['roomid'], "scores": scores_template})
  
def score(request):
    heart_rate = int(request.GET["heartRate"])
    miles = float(request.GET["miles"])
    
    roomid = request.session["roomid"]
    username = request.session['username']
    
    user = User.objects.filter(username=username)[0]
    minigame = MiniGame.objects.filter(name=roomid)[0]
    
    score = Score.objects.filter(user=user, game=minigame)
    
    if not score:
      new_score = Score(user=user, game=minigame, heart_rate=heart_rate, distance=miles, score=heart_rate*miles)
      new_score.save()
    else:
      score = score[0]
      score.miles = miles
      score.heart_rate = heart_rate
      score.score = int(heart_rate) * float(miles)
      score.save()
   
    return JsonResponse({'score': heart_rate*miles})
    
    

def authenticate(request):
  if request.GET['type'] == "GET":
    username = request.GET['username']
    request.session['username'] = username
    return JsonResponse({"Authorized": "True"})
  elif request.GET['type'] == "POST":
    username = request.GET['username']
    password = request.GET['password']
    new_user = User(username=username, password=password)
    new_user.save()
    request.session['username'] = username

    return JsonResponse({"Authorized": "True"})
    

def login(request):
    return render(request, 'life/main.html', {"username": request.session['username']})

def signup(request):
    return render(request, 'life/main.html', {"username": request.session['username']})