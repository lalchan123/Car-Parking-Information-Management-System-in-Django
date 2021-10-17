from django.contrib import admin
from django.contrib.auth.models import User
from .models import Customer


# Register your models here.
#admin.site.register(User)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','phone_number','car_model','car_color','price','total_cost','register_name','card_number','reg_date','exit_date')
    list_filter = ('car_model',)
admin.site.register(Customer,CustomerAdmin)
