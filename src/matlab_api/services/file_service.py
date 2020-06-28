import os
import zipfile
import shutil
from django.conf import settings
from django.core.files.storage import FileSystemStorage


class FileService():
    """
    Class for Command line
    """
    def get_file_dir(self, app_name, uuid):
        # creating output file dir
        file_dir = settings.OUTPUT_ROOT_FOLDER
        if uuid is not None:
            file_dir = os.path.join(file_dir, str(app_name), str(uuid))
        return file_dir

    def store_posted_file(self, app_name, uuid, file):
        try:
            file_dir = self.get_file_dir(app_name=app_name, uuid=uuid)
            fs = FileSystemStorage(location=file_dir)

            stored_file = fs.save(file.name, file)
            return stored_file
        except:
            return False

    # Declare the function to return all file paths of the particular directory
    def retrieve_file_paths(self, file_dir):
        file_paths = []
        # Read all directory, subdirectories and file lists
        for root, directories, files in os.walk(file_dir):
            for filename in files:
                # Create the full filepath by using os module.
                file_path = os.path.join(root, filename)
                file_paths.append(file_path)
        return file_paths


    def make_zip_file(self, app_name, uuid):
        dir_name = self.get_file_dir(app_name=app_name, uuid=uuid)
        print(dir_name)
        zipped_file = shutil.make_archive(uuid, 'zip', dir_name)
        dest_zipped_file = os.path.join(settings.MEDIA_ROOT,  'temp', uuid + '.zip')
        moved_file = shutil.move(zipped_file, dest_zipped_file)
        return moved_file

        # file_paths = self.retrieve_file_paths(dir_name)
        #
        # # writing files to a zipfile
        # zipped_file_name = uuid + '.zip'
        # zip_file = zipfile.ZipFile(zipped_file_name, 'w')
        # with zip_file:
        #     # writing each file one by one
        #     for file in file_paths:
        #         zip_file.write(file)
        #     return zip_file



