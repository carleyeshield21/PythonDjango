from django.contrib import admin
from .models import Forma

# Register your models here.
class FormaAdmin(admin.ModelAdmin):


admin.site.register(Forma)
