from django.contrib import admin
from .models import Worker,Location,PinCode,Service,Customer,Profile



admin.site.register(Profile)

class WorkerAdmin(admin.ModelAdmin):
  list_display = ("name", "pin", "mobile","work",)
admin.site.register(Worker, WorkerAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'contact', 'display_pin_codes','display_services')
    list_filter = ('place',)
    search_fields = ('name', 'place', 'contact')
    fields = ('name', 'place', 'contact', 'pin_codes', 'services')  # or use fieldsets if needed
    

    def display_pin_codes(self, obj):
        return ", ".join([pin_code.code for pin_code in obj.pin_codes.all()])
    admin.site.register(PinCode)

    def display_services(self,obj):
       return ",".join([services.name for services in obj.services.all()])
    admin.site.register(Service)
    display_pin_codes.short_description = 'Pin Codes'
    
admin.site.register(Location, LocationAdmin)

class CustomerAdmin(admin.ModelAdmin):
  list_display = ("name", "mobile","email" ,"address_line_1","address_line_2","city","state","postal_code","worker_name","worker_number","worker_work","date","approved")
  
  actions = ['enable_approval', 'disable_approval']

  def enable_approval(self, request, queryset):
        queryset.update(approved=True)

  enable_approval.short_description = 'Enable Approval'

  def disable_approval(self, request, queryset):
        queryset.update(approved=False)

  disable_approval.short_description = 'Disable Approval' 
  
admin.site.register(Customer, CustomerAdmin)
