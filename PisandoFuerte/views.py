from django.shortcuts import render, redirect

from .models import*
from .forms import*

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, "PisandoFuerte/index.html")

@login_required
def nike(request):
    contexto= {'nike':Nike.objects.all()}
    return render(request, "PisandoFuerte/Nike.html",contexto)

@login_required
def adidas(request):
    contexto= {'adidas':Adidas.objects.all()}
    return render(request, "PisandoFuerte/Adidas.html",contexto)

@login_required
def puma(request):
    contexto= {'puma':Puma.objects.all()}
    return render(request, "PisandoFuerte/Puma.html",contexto)

@login_required
def remeras(request):
    contexto= {'remeras':Remeras.objects.all()}
    return render(request, "PisandoFuerte/Remeras.html",contexto)

#__________________________________Forms
#def zapatillaForm(request):
    if request.method == "POST":
        miForm = ZapatillaForm(request.POST)
        if miForm.is_valid():
            zapatilla_modelo=miForm.cleaned_data.get("modelo")
            zapatilla_talle=miForm.cleaned_data.get("talle")
            zapatilla = Adidas(modelo=zapatilla_modelo, talle=zapatilla_talle)
            zapatilla.save()
            
            contexto= {'adidas':Adidas.objects.all()}
            return render(request, "PisandoFuerte/Adidas.html",contexto)
    else:
        miForm= ZapatillaForm()
        
    return render(request, "PisandoFuerte/zapatillaForm.html", {"form":miForm})

#def nikeform(request):
    if request.method == "POST":
        miForm = NikeForm(request.POST)
        if miForm.is_valid():
            nike_modelo=miForm.cleaned_data.get("modelo")
            nike_talle=miForm.cleaned_data.get("talle")
            nike = Nike(modelo=nike_modelo, talle=nike_talle)
            nike.save()
            
            contexto= {'nike':Nike.objects.all()}
            return render(request, "PisandoFuerte/Nike.html",contexto)
    else:
        miForm= NikeForm()
        
    return render(request, "PisandoFuerte/nikeForm.html", {"form":miForm})

#def pumaform(request):
    if request.method == "POST":
        miForm = PumaForm(request.POST)
        if miForm.is_valid():
            puma_modelo=miForm.cleaned_data.get("modelo")
            puma_talle=miForm.cleaned_data.get("talle")
            puma = Puma(modelo=puma_modelo, talle=puma_talle)
            puma.save()
            
            contexto= {'puma':Puma.objects.all()}
            return render(request, "PisandoFuerte/Puma.html",contexto)
    else:
        miForm= PumaForm()
        
    return render(request, "PisandoFuerte/pumaForm.html", {"form":miForm})

#def remerasform(request):
    if request.method == "POST":
        miForm = RemerasForm(request.POST)
        if miForm.is_valid():
            remeras_color=miForm.cleaned_data.get("color")
            remeras_talle=miForm.cleaned_data.get("talle")
            remeras = Remeras(color=remeras_color, talle=remeras_talle)
            remeras.save()
            
            contexto= {'remeras':Remeras.objects.all()}
            return render(request, "PisandoFuerte/Remeras.html",contexto)
    else:
        miForm= RemerasForm()
        
    return render(request, "PisandoFuerte/remerasForm.html", {"form":miForm})

#________________________________Buscar
@login_required
def buscar(request):
    return render (request, "PisandoFuerte/buscar.html")

@login_required
def encontrar(request):
    if request.GET["buscar"]:
        patron=request.GET["buscar"]
        zapatillas=Adidas.objects.filter(modelo__icontains=patron)
        contexto = {"adidas":zapatillas}
        return render(request, "PisandoFuerte/Adidas.html",contexto)
    
        
    contexto= {'adidas':Adidas.objects.all()}
    return render(request, "PisandoFuerte/Adidas.html",contexto)

#_________________________________________Nike

class NikeList(LoginRequiredMixin,ListView):
    model = Nike
    
class NikeCreate(LoginRequiredMixin,CreateView):
    model = Nike
    fields = ["modelo", "talle"]
    success_url = reverse_lazy("Nike")
    
class NikeUpgrade(LoginRequiredMixin,UpdateView):
    model = Nike
    fields = ["modelo", "talle"]
    success_url = reverse_lazy("Nike")
    
class NikeDelete(LoginRequiredMixin,DeleteView):
    model = Nike
    success_url = reverse_lazy("Nike")
    
#______________________________________Adidas
    
class AdidasList(LoginRequiredMixin,ListView):
    model = Adidas
    
class AdidasCreate(LoginRequiredMixin,CreateView):
    model = Adidas
    fields = ["modelo", "talle"]
    success_url = reverse_lazy("Adidas")
    
class AdidasUpgrade(LoginRequiredMixin,UpdateView):
    model = Adidas
    fields = ["modelo", "talle"]
    success_url = reverse_lazy("Adidas")
    
class AdidasDelete(LoginRequiredMixin,DeleteView):
    model = Adidas
    success_url = reverse_lazy("Adidas")
    
#______________________________________Puma
    
class PumaList(LoginRequiredMixin,ListView):
    model = Puma
    
class PumaCreate(LoginRequiredMixin,CreateView):
    model = Puma
    fields = ["modelo", "talle"]
    success_url = reverse_lazy("Puma")
    
class PumaUpgrade(LoginRequiredMixin,UpdateView):
    model = Puma
    fields = ["modelo", "talle"]
    success_url = reverse_lazy("Puma")
    
class PumaDelete(LoginRequiredMixin,DeleteView):
    model = Puma
    success_url = reverse_lazy("Puma")
    
#______________________________________Remeras
    
class RemerasList(LoginRequiredMixin,ListView):
    model = Remeras
    
class RemerasCreate(LoginRequiredMixin,CreateView):
    model = Remeras
    fields = ["color", "talle"]
    success_url = reverse_lazy("Remeras")
    
class RemerasUpgrade(LoginRequiredMixin,UpdateView):
    model = Remeras
    fields = ["color", "talle"]
    success_url = reverse_lazy("Remeras")
    
class RemerasDelete(LoginRequiredMixin,DeleteView):
    model = Remeras
    success_url = reverse_lazy("Remeras")
    
#______________________________________Login, Logout, Authentication, Registracion

def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user= authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request,user)
            
            #___Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"]=avatar
            #_____________________________________________________
            return render(request, "PisandoFuerte/index.html")
        else:
            return redirect(reverse_lazy('login'))
            
    else:
        miForm= AuthenticationForm()
        
    return render(request, "PisandoFuerte/login.html", {"form":miForm})

def register (request):
    if request.method == "POST":
        miForm=RegistroForm(request.POST)
        
        if miForm.is_valid():
            usuario  = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
            
    else:
        miForm= RegistroForm()
        
    return render(request, "PisandoFuerte/registro.html", {"form":miForm})

#____________________________Edicion de perfil, cambio de clave, avatar

@login_required
def editProfile(request):
    
    usuario = request.user
    
    if request.method == "POST":
        miForm=UserEditForm(request.POST)
        
        if miForm.is_valid():
            user= User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            
            user.save()
            return redirect(reverse_lazy('home'))
            
    else:
        miForm= UserEditForm(instance=usuario)
        
    return render(request, "PisandoFuerte/registro.html", {"form":miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "PisandoFuerte/cambiar_clave.html"
    success_url = reverse_lazy("home")
    
@login_required
def agregarAvatar(request):
   
    if request.method == "POST":
        miForm=AvatarForm(request.POST,request.FILES)
        
        if miForm.is_valid():
            usuario= User.objects.get(username=request.user)
            #_____________Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo)>0:
                for i in range (len(avatarViejo)):
                    avatarViejo[i].delete()
            #______________________________________
            avatar = Avatar(user=usuario, imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen= Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"]= imagen
            
            #print(f"{imagen}")
            return redirect(reverse_lazy('home'))
            
    else:
        miForm= AvatarForm()
        
    return render(request, "PisandoFuerte/agregarAvatar.html", {"form":miForm})

def about_me(request):
    return render(request, 'PisandoFuerte/about_me.html')


