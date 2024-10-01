from django.shortcuts import render, redirect, reverse
from accounts.models import User
from games.models import Game
from .models import Orders
from .forms import OrdersForm


# Create your views here.
def request_order(request, user_id, game_id):
    user = User.objects.get(id=user_id)
    game = Game.objects.get(id=game_id)

    if request.method == "GET":
        return render(
            request, "orders/index.html", context={"user": user, "game": game}
        )

    elif request.method == "POST":
        order = Orders(
            users=user,
            games=game,
            status="Delivered" if not game.price else "Processing",
        )
        order.save()

        url = reverse("details_page", args=[game.id])
        return redirect(url)


def resolve_orders(request):
    form = OrdersForm()
    orders = Orders.objects.all()

    if request.method == "GET":
        return render(
            request, "orders/admin_panel.html", context={"orders": orders, "form": form}
        )

    elif request.method == "POST":
        Orders.objects.filter(id=request.POST.get("id")).update(
            status=request.POST.get("status")
        )

        url = reverse("resolve_orders")
        return redirect(url)
