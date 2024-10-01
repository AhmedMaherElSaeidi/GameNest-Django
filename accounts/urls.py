from django.urls import path, include
from .views import profile, RegisterView

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("profile/", profile, name="profile"),
    path("signup/", RegisterView.as_view(), name="signup"),
]
