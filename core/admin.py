from django.contrib import admin
from .models import *
admin.site.site_header = "Khoeletso ea Lihoai"
admin.site.register(User)
admin.site.register(Farmer)
admin.site.register(Product)

# Register your models here
