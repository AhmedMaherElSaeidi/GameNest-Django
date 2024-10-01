from django.shortcuts import render, redirect, reverse
from .models import Category
from .forms import CategoryForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def index(request):
    categories = Category.objects.all()
    delete = request.GET.get("delete")
    return render(request, "categories/index.html", context={"categories": categories, "delete": delete})

class CreateCategory(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "categories/category_form.html"
    form_class = CategoryForm
    success_url = "/categories"

class EditCategory(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = "categories/category_form.html"
    form_class = CategoryForm
    success_url = "/categories"

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_category(request, category_id):
    Category.objects.get(id=category_id).delete()
    url = reverse('categories_page')
    return redirect(url + "?delete=success")