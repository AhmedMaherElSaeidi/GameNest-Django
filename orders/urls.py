from django.urls import path
from .views import request_order, resolve_orders

urlpatterns = [
    path("<int:user_id>/<int:game_id>", request_order, name="request_order"),
    path("admin", resolve_orders, name="resolve_orders"),
]
