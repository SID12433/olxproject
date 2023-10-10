"""
URL configuration for olx project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from task.views import VehicleCreateView,VehicleListView,VehicleDeleteView,VehicleDetailView,VehicleUpdateView,SignUpView,SignInView,signout_view,HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",HomePageView.as_view(),name="home"),
    path('vehicles/add/',VehicleCreateView.as_view(),name="vehicle-add"),
    path('vehicles/all/',VehicleListView.as_view(),name="vehicle-list"),
    path('vehicles/<int:pk>/remove/',VehicleDeleteView.as_view(),name="vehicle-remove"),
    path('vehicles/<int:pk>/detail/',VehicleDetailView.as_view(),name="vehicle-detail"),
    path('vehicles/<int:pk>/edit/',VehicleUpdateView.as_view(),name="vehicle-edit"),
    path("registration",SignUpView.as_view(),name="register"),
    path("login",SignInView.as_view(),name="login"),
    path("logout",signout_view,name="logout"),
    path("v1/olx/",include("remainder.urls"))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
