from django.contrib import admin

from .models import Brand, Perfum, Bottle

admin.site.register(Perfum)
admin.site.register(Brand)
admin.site.register(Bottle)
