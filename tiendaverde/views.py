from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.http import JsonResponse
import json

from .form import CustomUserRegister
from .models import Producto, Carrito, CarritoItem

def index(request):
    context={}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context, request))

def register_view(request):
    if request.method == "POST":
        form = CustomUserRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CustomUserRegister()
    return render(request, 'register.html', { "form":form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def catalogo_view(request):
    productos = Producto.objects.order_by("nombre")
    template = loader.get_template("catalogo.html")
    context = {
        "productos": productos,
    }
    return HttpResponse(template.render(context, request))



#CARRITO COSAS

def catalogo(request):
    productos = Producto.objects.all()

    if request.user.is_authenticated:
        carrito, created = Carrito.objects.get_or_create(usuario=request.user, completado=False)

    context = {"productos":productos}
    return render(request, "catalogo.html", context)


def carrito(request):
    if not request.user.is_authenticated:
        redirect("")

    carrito, created = Carrito.objects.get_or_create(usuario=request.user, completado=False)
    cosas_del_carrito = carrito.cosas_del_carrito.all()

    context = {"carrito":carrito, "items":cosas_del_carrito}
    return render(request, "carrito.html", context)

def agregarCarrito(request, pk):
    if not request.user.is_authenticated:
        redirect("")

    product_id = pk
    product = Producto.objects.get(ide=product_id)

    cart, created = Carrito.objects.get_or_create(usuario=request.user, completado=False)
    cosas_del_carrito, created =CarritoItem.objects.get_or_create(carrito=cart, producto=product)
    cosas_del_carrito.cantidad += 1
    cosas_del_carrito.save()

    return redirect("carrito")

def remover_del_carrito(request, pk):
    if not request.user.is_authenticated:
        redirect("")

    product_id = pk
    product = Producto.objects.get(ide=product_id)

    cart, created = Carrito.objects.get_or_create(usuario=request.user, completado=False)
    cosas_del_carrito, created =CarritoItem.objects.get_or_create(carrito=cart, producto=product)
    cosas_del_carrito.cantidad -= 1
    cosas_del_carrito.save()
    if cosas_del_carrito.cantidad <= 0:
        cosas_del_carrito.delete()

    return redirect("carrito")


def confirmar_pedido(request):
    if not request.user.is_authenticated:
        redirect("")

    cart, created = Carrito.objects.get_or_create(usuario=request.user, completado=False)
    if cart.cantidad_de_cosas <= 0:
        return redirect("")

    cart.completado = True
    cart.save()

    context = {"carrito":cart}
    return render(request, "confirmacion_carrito.html", context)
