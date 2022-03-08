from django.shortcuts import render,HttpResponse

# Create your views here.
def inicio(request):
    #return HttpResponse("<h1>Bienvenido a mi Sitio Web</h1>")
    return render(request, "inicio.html")

def cargo(request):
    #return HttpResponse("<h1>Mantenimiento De Cargos...</h1>")
    return render(request,"pages/cargo.html")

def departamento(request):
    #return HttpResponse("<h1>Mantenimiento De departamentos</h1>")
    return render(request,"pages/departamento.html")
def empleado(request):
    #return HttpResponse("<h1>Mantenimiento De Empleados</h1>")
    return render(request,"pages/empleado.html")

