from django.contrib import admin
from .models import Item

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'item_price', 'user_name')

admin.site.register(Item, ItemAdmin)