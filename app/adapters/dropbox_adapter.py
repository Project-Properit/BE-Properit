import dropbox
from dropbox.files import WriteMode


class DropboxAdapter:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_to_upload, upload_file_path):
        dbx = dropbox.Dropbox(self.access_token)
        dbx.files_upload(file_to_upload, upload_file_path, mode=WriteMode.overwrite)
        return dbx.sharing_create_shared_link_with_settings(upload_file_path).url.replace('?dl=0', '?raw=1')

    def update_file(self, file_to_upload, upload_file_path):
        dbx = dropbox.Dropbox(self.access_token)
        dbx.files_upload(file_to_upload, upload_file_path, mode=WriteMode.overwrite)
