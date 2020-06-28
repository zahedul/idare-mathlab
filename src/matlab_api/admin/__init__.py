from django.contrib import admin
from ..models import MatlabLogModel
from .matlab_log_admin import MatlabLogModelAdmin

admin.site.register(MatlabLogModel, MatlabLogModelAdmin)

