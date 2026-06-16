#from django.contrib import admin
#from .models import Order, OrderItem
#
#
#class OrderItemInline(admin.TabularInline):
#    model = OrderItem
#    extra = 0
#
#
#@admin.action(description="Mark selected orders as shipped")
#def mark_as_shipped(modeladmin, request, queryset):
#    queryset.update(status="shipped")
#
#
#@admin.register(Order)
#class OrderAdmin(admin.ModelAdmin):
#
#    list_display = (
#        "id",
#        "customer",
#        "status",
#        "total_price",
#        "created_at",
#    )
#
#    list_filter = (
#        "status",
#        "created_at",
#    )
#
#    search_fields = (
#        "customer",
#    )
#
#    readonly_fields = (
#        "created_at",
#        "total_price",
#    )
#
#    inlines = [OrderItemInline]
#
#    actions = [mark_as_shipped]