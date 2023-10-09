from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from remainder.views import SignUpView,SignInView,VehicleCreateView,VehicleListView,VehicleDetailView,VehicleUpdateView,remove_vehicle,signout_view



urlpatterns=[

    path("signup/",SignUpView.as_view(),name="signup"),
    path("signin/",SignInView.as_view(),name="signin"),
    path("add/",VehicleCreateView.as_view(),name="add-vehicle"),
    path("all/",VehicleListView.as_view(),name="list-vehicle"),
    path("<int:pk>/",VehicleDetailView.as_view(),name="detail-vehicle"),
    path("<int:pk>/change",VehicleUpdateView.as_view(),name="change-vehicle"),
    path("<int:pk>/remove",remove_vehicle,name="remove-vehicle"),
    path("signout/",signout_view,name="signout"),
       

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)