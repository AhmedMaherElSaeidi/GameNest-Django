from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="store_page"),
    path("<int:id>/", details, name="details_page"),
    path("add", CreatGame.as_view(), name="add_game"),
    path("edit/<pk>", EditGame.as_view(), name="edit_game"),
    path("delete/<int:game_id>", delete_game, name="delete_game"),
]
