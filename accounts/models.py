from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator


# Create your models here.
class User(AbstractUser):
    phone = models.CharField(
        validators=[MinLengthValidator(11), MaxLengthValidator(11)]
    )
    image = models.ImageField(upload_to="accounts/")
    join_date = models.DateField(default=timezone.now)
