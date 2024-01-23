from django.urls import path
from . import  views

urlpatterns = [
    path("plotPerDistrict/", views.plotPerDistrict, name="plotPerDistrict"),
    path("dataPerDistrict/",views.dataPerDistrict,name="dataPerDistrict"),
    path("plotPerLanguage/", views.plotPerLanguage, name="plotPerLanguage"),
    path("dataPerLanguage/",views.dataPerLanguage,name="dataPerLanguage"),
    
    
    path("",views.index,name="index")
]
