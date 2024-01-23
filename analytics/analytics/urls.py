from .views import index
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("",index, name="analyticsHome"),
    path("/",index, name="analyticsHome"),
    path("schools/",include("schools.urls")),
    # path("ipl/",include("ipl.urls") ),
    path('admin/', admin.site.urls),
]
