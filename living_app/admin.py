from django.contrib import admin
from living_app.models import property,property_details,property_interior_img
# Register your models here.

admin.site.register(property)
admin.site.register(property_details)
admin.site.register(property_interior_img)
