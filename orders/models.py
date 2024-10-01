from django.db import models
from games.models import Game
from accounts.models import User


# Create your models here.
class Orders(models.Model):
    STATUS_CHOICES = [
        ("Received", "Received"),
        ("Processing", "Processing"),
        ("Delivered", "Delivered"),
    ]

    users = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="users", null=True
    )
    games = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name="games", null=True
    )
    status = models.CharField(choices=STATUS_CHOICES, default="Processing")

    def __str__(self):
        return f"{self.id}_{self.users.first_name}_{self.games.name}"
