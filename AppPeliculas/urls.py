from django.urls import path
from AppPeliculas.views import *
from django.contrib.auth.views import LogoutView
from AppPeliculas import views

urlpatterns = [
    path("", inicio, name="Inicio"),

    #Autentificacion de usuario
    path("registro/", registro, name="registro"),
    path("iniciarSesion/", iniciarSesion, name="iniciarSesion"),
    path("salirSesion/", LogoutView.as_view(template_name="AppPeliculas/autentificacion/logout.html"), name="CerrarSesion"),
    path("agregarImagen/", views.agregarImagen, name="SubirAvatar"),
    path("buscarPelicula/", buscarPelicula, name="buscarPelicula"),
    path("resultados/", resultados),
   
    
    #CRUD Peliculas usando clases
    path("peliculas/lista", ListaPeliculas.as_view(), name="ListaPeliculas"),
    path("peliculas/<int:pk>", ActualizarPeliculas.as_view(), name="ActualizarPeliculas"),
    path("peliculas/crear", CrearPeliculas.as_view(), name="CrearPeliculas"),
    path("peliculas/borrar/<int:pk>", BorrarPeliculas.as_view(), name="BorrarPeliculas"),


    #CRUD Actor usando clases
    path("actor/lista", ListaActor.as_view(), name="ListaActor"),
    path("actor/<int:pk>", ActualizarActor.as_view(), name="ActualizarActor"),
    path("actor/crear", CrearActor.as_view(), name="CrearActor"),
    path("actor/borrar/<int:pk>", BorrarActor.as_view(), name="BorrarActor"),

    
    #CRUD Review usando clases
    path("review/lista", ListaReview.as_view(), name="ListaReview"),
    path("review/<int:pk>", ActualizarReview.as_view(), name="ActualizarReview"),
    path("review/crear", CrearReview.as_view(), name="CrearReview"),
    path("review/borrar/<int:pk>", BorrarReview.as_view(), name="BorrarReview"),
]


#super user
#David
#python123


#David1
#iniciar159