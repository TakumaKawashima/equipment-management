from django.contrib import admin
from .models import Equipment, InventoryChange, OrderRequest


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'status', 'location', 'quantity']
    search_fields = ['name', 'category']
    fieldsets = [
        (None, {'fields': ['name', 'category', 'status', 'location', 'description', 'image', 'quantity']}),
    ]
class InventoryChangeAdmin(admin.ModelAdmin):
    list_display = ('equipment', 'user', 'old_quantity', 'new_quantity', 'timestamp')
    list_filter = ('equipment', 'user', 'timestamp')

class OrderRequestAdmin(admin.ModelAdmin):
    list_display = ('equipment', 'user', 'quantity_requested', 'request_date', 'status', 'approved')
    list_filter = ('status', 'approved')
    search_fields = ('equipment__name', 'user__username')

admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(InventoryChange, InventoryChangeAdmin)
admin.site.register(OrderRequest, OrderRequestAdmin)
