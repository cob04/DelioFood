from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'email', 'phone',
                    'total_cost', 'paid', 'updated']
    list_filter = ['paid', 'created', 'updated']
    list_editable = ['paid']
    inlines = [OrderItemInline]
