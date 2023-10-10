from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from remainder.forms import RegistrationForm,LoginForm,VehicleCreateForm,VehicleChangeForm
from django.views.generic import View,ListView,DetailView,UpdateView,TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from remainder.models import Vehicles
from django.utils.decorators import method_decorator



def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session, please login to your account")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper


class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"signup.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration completed successfully")
            return redirect("signin")
        else:
            messages.error(request,"Registration failed")
            return render(request,"signup.html",{"form":form})      


class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"signin.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login success")
                return redirect("list-vehicle")
            else:
                messages.error(request,"invalid credentials !")
                return render(request,"signin.html",{"form":form})
            

@method_decorator(signin_required,name="dispatch")           
class VehicleCreateView(View):
    def get(self,request,*args,**kwargs):
        form=VehicleCreateForm()
        return render(request,"remainder/vehicle_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=VehicleCreateForm(request.POST)
        if form.is_valid():
            # form.save()
            Vehicles.objects.create(**form.cleaned_data,user=request.user)
            messages.success(request,"Added success")
            return redirect("add-vehicle")
        else:
            messages.error(request,"insertion failed")
            return render(request,"remainder/vehicle_add.html",{"form":form})

@method_decorator(signin_required,name="dispatch")           
class VehicleListView(ListView):
    template_name="remainder/vehicle_list.html"
    context_object_name="vehicles"
    model=Vehicles
    
    def get_queryset(self):
        qs=Vehicles.objects.filter(user=self.request.user)
        return qs
 
@method_decorator(signin_required,name="dispatch")              
class VehicleDetailView(DetailView):
    template_name="remainder/vehicle_detail.html"
    context_object_name="vehicle"
    model=Vehicles
    
@method_decorator(signin_required,name="dispatch")               
class VehicleUpdateView(UpdateView):
    template_name="remainder/vehicle_edit.html"
    success_url=reverse_lazy("list-vehicle")
    form_class=VehicleChangeForm
    model=Vehicles
    
@signin_required
def remove_vehicle(request,*args,**kwargs):
    id=kwargs.get("pk")
    Vehicles.objects.get(id=id).delete()
    return redirect("list-vehicle")

@signin_required
def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

    