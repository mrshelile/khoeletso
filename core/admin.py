from django.contrib import admin
from .models import *
admin.site.site_header = "Khoeletso ea Lihoai"
admin.site.register(User)
admin.site.register(Farmer)

# Register your models here.
