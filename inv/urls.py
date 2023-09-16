from django.urls import path
from inv.views import(
    Categoryview,
    CategoryCreate,
    CategoryUpdate,
    CategoryDelete,
    ProductView,
    ProductCreate,
    ProductDelete,
    ProductUpdate
)

urlpatterns = [
    path('category/', Categoryview.as_view(), name="category"),
    path('category/create/', CategoryCreate.as_view(), name="category_create"),
    path('category/edit/<int:pk>', CategoryUpdate.as_view(), name="category_update"),
    path('category/delete/<int:pk>', CategoryDelete.as_view(), name="category_delete"),

    path('product/', ProductView.as_view(), name="product"),
    path('product/create/', ProductCreate.as_view(), name="product_create"),
    path('product/edit/<int:pk>', ProductUpdate.as_view(), name="product_update"),
    path('product/delete/<int:pk>', ProductDelete.as_view(), name="product_delete")
]