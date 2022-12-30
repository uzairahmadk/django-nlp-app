from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import forms
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import redirect,render
import pandas as pd

# Register your models here
from .models import  Department,Supervision,Technology,Announcement,Project as ProjectDB

admin.site.register(Department)
admin.site.register(Supervision)
admin.site.register(Technology)
admin.site.register(Announcement)
class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

@admin.register(ProjectDB)
class Project(admin.ModelAdmin):
    list_filter = ('name', 'technology','supervisor','created')
    list_display = ['name', 'technology','supervisor','created']
    search_fields = ['name', 'technology__tech','supervisor__supervisor','created']

    change_list_template = "change_list.html"
    try:
        def get_urls(self):
            urls = super().get_urls()
            my_urls = [
                path('import-csv/', self.import_csv),
            ]
            return my_urls + urls
        def import_csv(self, request):
            if request.method == "POST":
                csv_file = request.FILES["csv_file"] 
                reader = pd.read_csv(csv_file)
                reader = reader.fillna("")
                for rows in reader.values.tolist():
                    proj = ProjectDB.objects.create(                            
                        name = rows[0] if rows[0] else None,
                        department =  Department.objects.get_or_create(dept=rows[1])[0],
                        supervisor =  Supervision.objects.get_or_create(supervisor=rows[2])[0],
                        technology =  Technology.objects.get_or_create(tech=rows[3])[0],
                    )
                    # proj.save()
                self.message_user(request, "Your csv file has been imported")   
                return redirect("..")
            form = CsvImportForm()
            payload = {"form": form}
            return render(
                request, "csv_form.html", payload
            )
    except Exception as ex:
        print("New Function Exception: ",ex)
