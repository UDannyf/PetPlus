# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Raza)
admin.site.register(TipoMascota)
admin.site.register(Mascota)
admin.site.register(Local)
admin.site.register(Recomendar)
admin.site.register(Cuidado)
admin.site.register(Planificacion)
