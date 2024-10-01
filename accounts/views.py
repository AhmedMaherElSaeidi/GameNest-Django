from .models import User
from .forms import UserForm
from orders.models import Orders
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def profile(request):
    orders = Orders.objects.filter(users=request.user)
    return render(request, "accounts/profile.html", context={"orders": orders})


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    template_name = "accounts/signup.html"
    success_url = "/index/"

    # Validate form
    # after that it will call form_valid function: write to database
    def form_valid(self, form):
        user = form.save(commit=False)
        user.password = make_password(user.password)
        user.save()
        return redirect(self.success_url)
