from django.contrib import admin

from schedule.models import Schedule

from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.
class ScheduleResource(resources.ModelResource):
    class meta:
        model = Schedule

@admin.register(Schedule)
class ScheduleAdmin(ImportExportModelAdmin):
    resource_class = ScheduleResource
    list_display = ['date']
    list_filter = ['date']
