import os
import uuid


def __files_unique_path(instance, filename, folder_name='docs'):
    # file will be uploaded to MEDIA_ROOT/<folder_name>/<filename>
    _, ext = os.path.splitext(filename)
    return f"{folder_name}/{uuid.uuid4()}{ext}"


def document_path(instance, filename):
    return __files_unique_path(instance, filename, folder_name='documents')
