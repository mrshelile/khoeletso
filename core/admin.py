from django.contrib import admin
from .models import *
import pandas as pd
import matplotlib.pyplot as plt

admin.site.site_header = "Khoeletso ea Lihoai"
admin.site.register(User)
admin.site.register(Farmer)
# admin.site.register(Product)

# Register your models here.
@admin.action(description='Analytics')
def make_analyse(modeladmin, request, queryset):
    # users=[]
    # for element in queryset.values():
        # print(element)
    # print(queryset.values())
    # df = pd.DataFrame(queryset.values())
    # df.drop("id",axis=1,inplace=True)
    # newdf = df.reset_index(drop=True).set_index("created")
    # df1 =newdf['rate']
    # print(df1.head(5))
    # df1.plot()
    # plt.show()
    pass
         
class ProductAdmin(admin.ModelAdmin):
    # list_display = ['title', 'status']
    # ordering = ['title']
    actions = [make_analyse]
admin.site.register(Product, ProductAdmin)
# Register your models here
