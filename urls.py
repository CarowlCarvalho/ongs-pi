from django.urls import path
from galeria.views import index, cadastro, login, participa, artigos, perfil

urlpatterns = [
    path('', index),
    path('cadastro/', cadastro),
    path('login/', login),
    path('participa/', participa),
    path('artigos/', artigos),
    path('perfil/', perfil),



]