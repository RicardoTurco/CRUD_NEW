"""teste004 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from T004.views import home, listCategorias, novaCategoria, upCategoria, deleteCat,\
    listTransacoes, novaTransacao, upTransacao, deleteTrans

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('listCategorias/', listCategorias, name='listCategorias'),
    path('novaCategoria', novaCategoria, name='novaCategoria'),
    path('upCategoria/<int:pk>/', upCategoria, name='upCategoria'),
    path('deleteCat/<int:pk>', deleteCat, name='deleteCat'),
    path('listTransacoes/', listTransacoes, name='listTransacoes'),
    path('novaTransacao/', novaTransacao, name='novaTransacao'),
    path('upTransacao/<int:pk>/', upTransacao, name='upTransacao'),
    path('deleteTrans/<int:pk>', deleteTrans, name='deleteTrans')
]
