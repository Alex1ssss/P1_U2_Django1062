from django.shortcuts import render, redirect
from .models import Ventas
# Create your views here.

def inicio_vista(request):
    lasVentas=Ventas.objects.all

    return render(request,"gestionarMateria.html", {"misventas":lasVentas})

def registrarVenta(request):
    codigo=request.POST["txtcodigo"]
    id_cliente=request.POST["txtcliente"]
    fecha=request.POST["txtfecha"]
    total_venta=request.POST["txttotal"]
    metodo_pago=request.POST["txtmetodo"]
    id_empleado=request.POST["txtempleado"]
    guardarVenta=Ventas.objects.create(codigo=codigo, fecha=fecha,total_venta=total_venta, id_cliente=id_cliente, metodo_pago=metodo_pago, id_empleado=id_empleado)
    return redirect("/")

def seleccionarVenta(request,codigo):
    ventas=Ventas.objects.get(codigo=codigo)
    return render(request, "editarMateria.html", {"misventas": ventas})

def editarVentas(request):
    codigo=request.POST["txtcodigo"]
    id_cliente=request.POST["txtcliente"]
    fecha=request.POST["txtfecha"]
    total_venta=request.POST["txttotal"]
    metodo_pago=request.POST["txtmetodo"]
    id_empleado=request.POST["txtempleado"]
    ventas=Ventas.objects.get(codigo=codigo)
    ventas.codigo=codigo
    ventas.id_cliente=id_cliente
    ventas.fecha=fecha
    ventas.total_venta=total_venta
    ventas.metodo_pago=metodo_pago
    ventas.id_empleado=id_empleado
    ventas.save()
    return redirect("/")

def borrarVenta(request, codigo):
    ventas=Ventas.objects.get(codigo=codigo)
    ventas.delete()

    return redirect("/")