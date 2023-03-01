from django.shortcuts import render
from django.http import HttpResponse
from AppPeliculas.models import *
from AppPeliculas.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



#INICIO -------------------------------------

def inicio(request):
    return render(request, "AppPeliculas/inicio.html")


#REGISTRO -------------------------------------

def registro(request):

    if request.method == 'POST':
        
        miformulario = UserCreationForm(request.POST)

        if miformulario.is_valid():
                
            miformulario.save()

            return render(request, "AppPeliculas/inicio.html")       

    else:

        miformulario = UserCreationForm()

    return render(request, "AppPeliculas/autentificacion/registro.html",{"miFormulario":miformulario}) 


#INICAR SESION -------------------------------------

def iniciarSesion(request):

    if request.method == 'POST':

        miformulario = AuthenticationForm(request, data=request.POST)

        if miformulario.is_valid():

            username = miformulario.cleaned_data.get("username")
            password = miformulario.cleaned_data.get("password")

            miUsuario = authenticate(username=username, password=password)

            if miUsuario:

                login(request, miUsuario)

                mensaje = f"Bienvenido {miUsuario.username}"

                return render(request, "AppPeliculas/inicio.html", {"mensaje":mensaje})   
                
        mensaje = f"Error, ingresaste mal los datos."

        return render(request, "AppPeliculas/inicio.html", {"mensaje":mensaje}) 
    
    else:

        miformulario = AuthenticationForm()  

    return render(request, "AppPeliculas/autentificacion/login.html",{"miFormulario":miformulario})


#SUBIR AVATARES -------------------------------------

@login_required
def agregarImagen (request):

    if request.method == 'POST':

        miFormulario = AvatarFormulario (request. POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            avatar = Avatar (user=request.user, imagen=informacion['imagen'])

            avatar.save()

            return render(request, "AppPeliculas/inicio.html")
        
    else:

        miFormulario = AvatarFormulario()
        
        return render(request, "AppPeliculas/autentificacion/agregarImg.html", {'form':miFormulario})




#PELICULAS -------------------------------------

class ListaPeliculas(ListView):

    model = Peliculas
    template_name = "AppPeliculas//pelicula/pelicula_list.html"

class CrearPeliculas(LoginRequiredMixin, CreateView):
    
    model = Peliculas
    success_url = "/AppPeliculas/peliculas/lista"
    template_name = "AppPeliculas//pelicula/pelicula_form.html"
    fields = ["Nombre", "Genero", "Año", "Origen", "Duracion", "Director", "Cast", "Ranking"]

class ActualizarPeliculas(LoginRequiredMixin, UpdateView):

    model = Peliculas
    success_url = "/AppPeliculas/peliculas/lista"
    template_name = "AppPeliculas/pelicula/pelicula_form.html"
    fields = ["Nombre", "Genero", "Año", "Origen", "Duracion", "Director", "Cast", "Ranking"]

class BorrarPeliculas(LoginRequiredMixin, DeleteView):

    model = Peliculas
    success_url = "/AppPeliculas/peliculas/lista"
    template_name = "AppPeliculas//pelicula/pelicula_confirm_delete.html"

#ACTORES -------------------------------------

class ListaActor(ListView):

    model = Actor
    template_name = "AppPeliculas/actor/actor_list.html"

class CrearActor(LoginRequiredMixin, CreateView):
    
    model = Actor
    success_url = "/AppPeliculas/actor/lista"
    template_name = "AppPeliculas/actor/actor_form.html"
    fields = ["Nombre", "Cumpleaños", "Nacionalidad"]

class ActualizarActor(LoginRequiredMixin, UpdateView):

    model = Actor
    success_url = "/AppPeliculas/actor/lista"
    template_name = "AppPeliculas/actor/actor_form.html"
    fields = ["Nombre", "Cumpleaños", "Nacionalidad"]

class BorrarActor(LoginRequiredMixin, DeleteView):

    model = Actor
    success_url = "/AppPeliculas/actor/lista"
    template_name = "AppPeliculas/actor/actor_confirm_delete.html"


#REVIEW -------------------------------------

class ListaReview(ListView):

    model = Review
    template_name = "AppPeliculas/review/review_list.html"

class CrearReview(LoginRequiredMixin, CreateView):
    
    model = Review
    success_url = "/AppPeliculas/review/lista"
    template_name = "AppPeliculas/review/review_form.html"
    fields = ["Pelicula", "Autor", "Contenido", "Ranking"]

class ActualizarReview(LoginRequiredMixin, UpdateView):

    model = Review
    success_url = "/AppPeliculas/review/lista"
    template_name = "AppPeliculas/review/review_form.html"
    fields = ["Pelicula", "Autor", "Contenido", "Ranking"]

class BorrarReview(LoginRequiredMixin, DeleteView):

    model = Review
    success_url = "/AppPeliculas/review/lista"
    template_name = "AppPeliculas/review/review_confirm_delete.html"


#BUSCADOR -------------------------------------

def buscarPelicula(request):

    return render(request, "AppPeliculas/buscarPelicula.html")


def resultados(request):

    if request.method == "GET":

        nombreBusqueda = request.GET["Nombre"]

        resultadoPeliculas = Peliculas.objects.filter(Nombre__icontains=nombreBusqueda)

        return render(request, "AppPeliculas/resultados.html", {"info1":nombreBusqueda, "info2":resultadoPeliculas})
    
    return render(request, "AppPeliculas/resultados.html")
    
