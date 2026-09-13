from django.contrib.admin import site
from .models import Rol, PerfilUsuario

site.register(Rol)
site.register(PerfilUsuario)