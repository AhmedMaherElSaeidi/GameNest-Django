from django.shortcuts import render, redirect, reverse
from .models import Game
from .forms import GameForm
from orders.models import Orders
from accounts.models import User
from categories.models import Category
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index(request):
    genre = request.GET.get("genre")

    if genre:
        genre = genre.replace("%20", " ")
        category = Category.objects.get(name=genre)
        games = category.game_categories.all()
    else:
        games = Game.objects.all()
    delete = request.GET.get("delete")
    return render(request, "games/index.html", context={"games": games, "genre": genre, "delete": delete})


def details(request, id):
    game = Game.objects.get(id=id)
    if request.user.id:
        user = User.objects.get(id=request.user.id)
        has_ordered_game = Orders.objects.filter(users=user, games=game).exists()
    else:
        has_ordered_game = None
        user = None

    return render(
        request,
        "games/details.html",
        context={"game": game, "has_ordered_game": has_ordered_game},
    )

class CreatGame(LoginRequiredMixin, CreateView):
    model = Game
    template_name = "games/game_form.html"
    form_class = GameForm
    success_url = "/games"

class EditGame(LoginRequiredMixin, UpdateView):
    model = Game
    template_name = "games/game_form.html"
    form_class = GameForm
    success_url = "/games"

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_game(request, game_id):
    Game.objects.get(id=game_id).delete()
    url = reverse('store_page')
    return redirect(url + "?delete=success")