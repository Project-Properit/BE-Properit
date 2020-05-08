import dropbox
from dropbox.cloud_docs import GetMetadataError
from dropbox.exceptions import ApiError
from dropbox.files import WriteMode


class DropboxAdapter:
    def __init__(self, access_token):
        self.access_token = access_token
        self.dbx = dropbox.Dropbox(self.access_token)

    def upload_file(self, file_to_upload, upload_file_path):
        self.dbx.files_upload(file_to_upload, upload_file_path, mode=WriteMode.overwrite)
        return self.dbx.sharing_create_shared_link_with_settings(upload_file_path).url.replace('?dl=0', '?raw=1')

    def update_file(self, file_to_upload, upload_file_path):
        self.dbx.files_upload(file_to_upload, upload_file_path, mode=WriteMode.overwrite)
        return self.dbx.sharing_list_shared_links(upload_file_path).links[0].url.replace('?dl=0', '?raw=1')

    def check_file_existence(self, upload_file_path):
        try:
            if self.dbx.files_get_metadata(upload_file_path):
                return True
        except Exception as e:
            if isinstance(e.error, dropbox.files.GetMetadataError):
                return False
            else:
                raise
        # except LookupError:
        #     return False
        # except GetMetadataError:
        #     return False
        # except ApiError:
        #     return False

    def get_download_link(self, upload_file_path):
        return self.dbx.files_get_temporary_link(upload_file_path).link

