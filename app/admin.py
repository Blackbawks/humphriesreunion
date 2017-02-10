from django.contrib import admin
from django.db import models
from app.models import *


#class NumericAdmin(admin.ModelAdmin):
    #search_fields = ('species__species_id',)    

#class OtherAdmin(admin.ModelAdmin):
    #search_fields = ('species__species_id',)


admin.site.register(Mothers)
admin.site.register(Fathers)
admin.site.register(Person)


