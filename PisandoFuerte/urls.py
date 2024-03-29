
from django.urls import path, include
from .views import*
from . import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    #______________________________________Menu principal
    path('',home, name='home'),
    #path('Nike/',nike, name='Nike'),
    #path('Adidas/',adidas, name='Adidas'),
    #path('Puma/',puma, name='Puma'),
    #path('Remeras/',remeras, name='Remeras'),
    
    #______________________________________Formularios
    #path('zapatilla_form/',zapatillaForm,name="zapatilla_form"),
    #path('nike_form/',nikeform,name="nike_form"),
    #path('puma_form/',pumaform,name="puma_form"),
    #path('remeras_form/',remerasform,name="remeras_form"),
    
    #_____________________________________Busqueda
    path('buscar/',buscar,name="buscar"),
    path('encontrar/',encontrar,name="encontrar"),
    
     #_____________________________________Nike
    path('nike/',NikeList.as_view(),name="Nike"),
    path('nike_create/',NikeCreate.as_view(),name="nike_create"),
    path('nike_update/<int:pk>',NikeUpgrade.as_view(),name="nike_update"),
    path('nike_delete/<int:pk>',NikeDelete.as_view(),name="nike_delete"),
    
    
     #_____________________________________Adidas
    path('adidas/',AdidasList.as_view(),name="Adidas"),
    path('adidas_create/',AdidasCreate.as_view(),name="adidas_create"),
    path('adidas_update/<int:pk>',AdidasUpgrade.as_view(),name="adidas_update"),
    path('adidas_delete/<int:pk>',AdidasDelete.as_view(),name="adidas_delete"),
    
        #_____________________________________Puma
    path('puma/',PumaList.as_view(),name="Puma"),
    path('puma_create/',PumaCreate.as_view(),name="puma_create"),
    path('puma_update/<int:pk>',PumaUpgrade.as_view(),name="puma_update"),
    path('puma_delete/<int:pk>',PumaDelete.as_view(),name="puma_delete"),
    
    #_____________________________________Remeras
    path('remeras/',RemerasList.as_view(),name="Remeras"),
    path('remeras_create/',RemerasCreate.as_view(),name="remeras_create"),
    path('remeras_update/<int:pk>',RemerasUpgrade.as_view(),name="remeras_update"),
    path('remeras_delete/<int:pk>',RemerasDelete.as_view(),name="remeras_delete"),
    
    #______________________________________Login, Logout, Registracion
    path ('login/', login_request, name="login"),
    path ('logout/', LogoutView.as_view(template_name="PisandoFuerte/logout.html"), name="logout"),
    path ('registrar/', register, name="registar"),
    
    #_____________________________Edicion perfil, cambio de clave, Avatar
    path ('perfil/', editProfile, name="perfil"),
    path ('<int:pk>/password/', CambiarClave.as_view(), name="cambiar_clave"),
    path ('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
    
    #____________________________Acerca de Mi
    path('about/', views.about_me, name='about_me'),
]

