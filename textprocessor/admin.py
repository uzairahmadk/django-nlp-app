from django.contrib import admin

# Register your models here
from .models import  *

@admin.register(Project)
class Search(admin.ModelAdmin):
    list_display = ['name', 'technology','supervisor','created']
    list_filter = ('name', 'technology','supervisor','created')
    search_fields = ['name', 'technology','supervisor','created']

admin.site.register(Department)
admin.site.register(Supervision)
admin.site.register(Technology)