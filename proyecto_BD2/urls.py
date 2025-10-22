from django.contrib import admin
from django.urls import path
from sistema import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('menu/',views.menu),
    path('login/',views.iniciarSesion),
    path('logout/',views.cerrarSesion),
]
