from django.contrib import admin

# Register your models here.

from appCondominio.models import Casa, Condominio, Espacios_comunes, Usuario, Seguridad
admin.site.register(Casa)
admin.site.register(Condominio)
admin.site.register(Espacios_comunes)
admin.site.register(Usuario)
admin.site.register(Seguridad)



