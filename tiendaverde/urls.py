from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("catalogo/", views.catalogo, name="catalogo"),
    path("carrito/", views.carrito, name="carrito"),
    path("agregarCarrito/<uuid:pk>", views.agregarCarrito, name="agregar_carrito"),
    path("remover_del_carrito/<uuid:pk>", views.remover_del_carrito, name="remover_del_carrito"),
    path("confirmar_pedido/", views.confirmar_pedido, name="confirmar_pedido"),
]
