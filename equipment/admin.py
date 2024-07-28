from django.contrib import admin
from .models import Equipment

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'status', 'location', 'quantity']
    search_fields = ['name', 'category']
    fieldsets = [
        (None, {'fields': ['name', 'category', 'status', 'location', 'description', 'image', 'quantity']}),
    ]

admin.site.register(Equipment, EquipmentAdmin)
