import os
import matlab.engine as engine
from django.conf import settings

class CommandLineService():
    """
    Class for command line actions of matlab
    """
    def run_matlab_file(self, app_name, uuid, file_name):
        try:
            # creating output file dir
            file_dir = settings.OUTPUT_ROOT_FOLDER
            if uuid is not None:
                file_dir = os.path.join(file_dir, str(app_name), str(uuid))

            eng = engine.start_matlab()
            eng.cd(file_dir, nargout=0)
            func_name = file_name.split('.m')[0]
            getattr(eng, '{func_name}'.format(func_name=func_name))(nargout=0)
            return True
        except Exception as ex:
            print(ex)
            return ex
