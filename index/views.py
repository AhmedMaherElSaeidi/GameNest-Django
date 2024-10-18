from django.shortcuts import render
from games.models import Game


# Create your views here.
def index(request):
    recent_games = Game.objects.all()[::-1][:3]
    return render(request, "index/index.html", context={"games": recent_games})
