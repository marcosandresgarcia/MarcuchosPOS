from django.urls import path
from inv.views import Categoryview, CategoryCreate

urlpatterns = [
    path('', Categoryview.as_view(), name="category"),
    path('create/', CategoryCreate.as_view(), name="category_create")
]