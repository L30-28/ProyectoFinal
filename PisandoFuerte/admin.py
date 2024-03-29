from django.contrib import admin

# Register your models here.
from .models import*

class ModeloAdmin(admin.ModelAdmin):
    list_display = ("modelo", "talle")
    list_filter = ("modelo",)

admin.site.register(Nike, ModeloAdmin)
admin.site.register(Adidas, ModeloAdmin)
admin.site.register(Puma, ModeloAdmin)
admin.site.register(Remeras)