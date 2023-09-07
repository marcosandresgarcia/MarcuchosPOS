from django.urls import path
from inv.views import Categoryview, CategoryCreate, CategoryUpdate

urlpatterns = [
    path('', Categoryview.as_view(), name="category"),
    path('create/', CategoryCreate.as_view(), name="category_create"),
    path('edit/<int:pk>', CategoryUpdate.as_view(), name="category_update")
]