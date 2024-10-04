from django.contrib import admin 
# Register your models here. 
from .models import BoardsModel 
admin.site.site_header = 'Curso Django' 
admin.site.index_title = 'Panel de control Proyecto Django' 
admin.site.site_title = 'Administrador Django' 
class BoardsAdmin(admin.ModelAdmin): 
    readonly_fields = ('creado', 'modificado') 
    list_display = ('clasificacion', 'titulo', 'valor') 
    search_fields = ('titulo', 'descripcion') 
    ordering = ('valor',) 
    list_filter = ('creado','valor') 
    def clasificacion(self, obj): 
        return "Alto" if obj.valor >= 5 else "Bajo" 
admin.site.register(BoardsModel, BoardsAdmin)  