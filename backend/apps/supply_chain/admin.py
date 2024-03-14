from django.contrib import admin
from supply_chain.models import (
    Farmer, Processor, Product, Retailer
)

admin.site.register(Farmer)
admin.site.register(Processor)
admin.site.register(Retailer)
admin.site.register(Product)
