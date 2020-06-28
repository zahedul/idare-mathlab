from django.contrib import admin


class MatlabLogModelAdmin(admin.ModelAdmin):
    list_display = ('app_name', 'requested_uuid', 'requested_ip', 'file_name', 'created')
    fields = ('app_name', 'requested_uuid', 'requested_ip', 'file_name', 'dependency_files')