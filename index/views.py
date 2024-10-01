from django.shortcuts import render
from games.models import Game


# Create your views here.
def index(request):
    games = Game.objects.all()
    return render(request, "index/index.html", context={"games": games})
