from django.contrib import admin

from .models import Client,Shipment
# Register your models here.
admin.site.register(Shipment)

@admin.register(Client)
class ClientData(admin.ModelAdmin):
    list_display = ("Name_of_item", "Supplier", "Description_notes", "Expected_Date_Delivery","Status")
    list_filter = ("Name_of_item",)
    fields = ("Name_of_item", "Supplier", "Description_notes", "Expected_Date_Delivery","Status")