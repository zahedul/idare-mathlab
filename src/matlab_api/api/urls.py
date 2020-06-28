from django.urls import path
from ..views import MatlabView

urlpatterns = [
    path('<app_name>', MatlabView.as_view(), name='matlab_view'),
]
