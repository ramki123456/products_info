from django.contrib import admin

# Register your models here.

from myapp.models import StockDetails, Employe
admin.site.register(StockDetails)
admin.site.register(Employe)