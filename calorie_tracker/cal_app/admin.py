from django.contrib import admin
from .models import Food,Consume
# Register your models here.

admin.site.site_header = 'Calorie Tracker'
admin.site.site_title = 'Calorie Tracker'
admin.site.index_title = 'Manage Your Calories'

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name','calories','carbs','proteins','fats')
    search_fields = ('name',)

admin.site.register(Food,FoodAdmin)
admin.site.register(Consume)
