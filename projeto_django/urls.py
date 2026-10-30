
from django.contrib import admin
from django.urls import path
from meu_app.views import home, registrar_usuario, login_usuario, logout_usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('registro/', registrar_usuario, name='registro'),
    path('login/', login_usuario, name='login'),
    path('logout/', logout_usuario, name='logout'),
]
