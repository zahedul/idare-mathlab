from django.db import models
from django_extensions.db.models import TimeStampedModel


class MatlabLogModel(TimeStampedModel):
    """
    This MatlabLogModel keeps the track of
    files which are send for compiling.
    """
    app_name = models.CharField("App Name", max_length=255, null=True, blank=True)
    requested_uuid = models.CharField("UUID", max_length=255, null=True, blank=True)
    requested_ip = models.CharField("Requested IP", max_length=255, null=True, blank=True)
    file_name = models.CharField("File Name", max_length=255, null=True, blank=True)
    dependency_files = models.TextField("Dependent Files List", null=True, blank=True)

    def __str__(self):
        return '{app_name}-{uuid}'.format(app_name=self.app_name, uuid=self.requested_uuid)

