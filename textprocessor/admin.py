from django.contrib import admin

# Register your models here
from .models import  *

admin.site.register(Department)
admin.site.register(Supervision)
admin.site.register(Technology)
@admin.register(Project)
class Project(admin.ModelAdmin):
    list_filter = ('name', 'technology','supervisor','created')
    list_display = ['name', 'technology','supervisor','created']
    search_fields = ['name', 'technology__tech','supervisor__supervisor','created',]