from django.contrib import admin
from .models import Forma

# Register your models here.
class FormaAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname','email','trabaho','date')
    search_fields = ('firstname', 'lastname','email','trabaho','date')
    list_filter = ('date','trabaho')
    ordering = ('-lastname',)
    readonly_fields = ('lastname',)

admin.site.register(Forma, FormaAdmin)
