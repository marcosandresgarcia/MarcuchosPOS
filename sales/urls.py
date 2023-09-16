from django.urls import path

from sales.views import ClientsView, ClientsCreate, ClientsUpdate, CategoryDelete

urlpatterns = [
    path('clients/', ClientsView.as_view(), name="clients"),
    path('clients/create', ClientsCreate.as_view(), name="clients_create"),
    path('clients/update/<int:pk>', ClientsUpdate.as_view(), name="clients_update"),
    path('clients/delete/<int:pk>', CategoryDelete.as_view(), name="clients_delete"),

    # path('facturas/buscar-producto', ProductoView.as_view(), name="factura_producto"),
    #
    # path('facturas/borrar-detalle/<int:id>', borrar_detalle_factura, name="factura_borrar_detalle"),
    #
    # path('facturas/imprimir/<int:id>', imprimir_factura_recibo, name="factura_imprimir_one"),
    #
    # path('facturas/imprimir-todas/<str:f1>/<str:f2>', imprimir_factura_list, name="factura_imprimir_all"),
    #
    # path('facturas/clientes/new/', cliente_add_modify, name="fac_cliente_add"),
    # path('facturas/clientes/<int:pk>', cliente_add_modify, name="fac_cliente_mod")
]
