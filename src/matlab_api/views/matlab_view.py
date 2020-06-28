import shutil, os
from rest_framework.generics import ListCreateAPIView
from ..api.serializers import MatlabSerializer
from ..services import CommandLineService,FileService
from ..models import MatlabLogModel
from django.http import JsonResponse, HttpResponse


class MatlabView(ListCreateAPIView):
    serializer_class = MatlabSerializer

    def post(self,
             request,
             app_name,
             *args,
             **kwargs):
        """
        :param app_name: Name of the application which file has to be run.
        :return: the generated files in a {uuid}.zip format.
        """
        response = {}
        stored_files_list = []
        uuid = request.POST.get('uuid', False)
        no_of_dependency =  request.POST.get('no_of_dependency', False)
        if no_of_dependency:
            no_of_dependency = int(no_of_dependency)

        file = request.FILES.get('file', False)
        if file:
            stored_ml_file = FileService().store_posted_file(app_name=app_name, uuid=uuid, file=file)
        for i in range(no_of_dependency):
            dependency_file = request.FILES.get('dependency_' + str(i), False)
            if dependency_file:
                stored_files_list.append(
                    FileService().store_posted_file(app_name=app_name, uuid=uuid, file=dependency_file)
                )

        if stored_ml_file:
            log_data = {
                'app_name' : app_name,
                'requested_uuid' : uuid,
                'requested_ip' : request.META.get('REMOTE_ADDR', False),
                'file_name' : stored_ml_file,
                'dependency_files' : ', '.join(stored_files_list),
            }
            created_log = MatlabLogModel.objects.create(**log_data)
            matlab_ran = CommandLineService().run_matlab_file(app_name=app_name, uuid=uuid, file_name=stored_ml_file)
            if matlab_ran is True:
                zipped_file = FileService().make_zip_file(app_name=app_name, uuid=uuid)
                zip_file_name = '{uuid}.zip'.format(uuid=str(uuid))
                zipped_file_folder = os.path.dirname(zipped_file)
                with open(zipped_file, 'rb') as file:
                    response = HttpResponse(file, content_type='application/zip')
                    response['Content-Disposition'] = 'attachment; filename={file_name}.zip'.format(file_name=zip_file_name)
                    # shutil.rmtree(zipped_file_folder)
                    return response
            else:
                response['is_success'] = False
                response['errors'] = {
                    'message': 'File Did not run successfully!'
                }
        else:
            response['is_success'] = False
            response['errors'] = {
                'message' : 'File Did not store.'
            }
        response['is_success'] = False
        response['errors'] = {
            'message' : 'Hello.'
        }
        return JsonResponse(response)






