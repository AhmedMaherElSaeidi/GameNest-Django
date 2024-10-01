from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="categories_page"),
    path("add", CreateCategory.as_view(), name="add_category"),
    path("edit/<pk>", EditCategory.as_view(), name="edit_category"),
    path("delete/<int:category_id>", delete_category, name="delete_category"),
]
