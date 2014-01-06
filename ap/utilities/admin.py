from django import forms
from django.contrib import admin

from utilities.models import Location, Bill

# class UtilityAdminForm(forms.ModelForm):
#  
#      class Meta:
#          model = Location
#  
#  
# class UtilityAdmin(admin.ModelAdmin):
#      form = UtilityAdminForm
#      list_display = (
#          'name',
#          'customer_id',
#          'location_id',
#      )
#      ordering = ('name', 'location_id',)
#      search_fields = ['name', 'location_id',]
# 
# 
# admin.site.register(Location, UtilityAdmin)
admin.site.register(Location)
admin.site.register(Bill)