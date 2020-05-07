import dropbox


class DropboxAdapter:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_to_upload, upload_file_path):
        dbx = dropbox.Dropbox(self.access_token)
        dbx.files_upload(file_to_upload, upload_file_path)
        return dbx.sharing_create_shared_link(upload_file_path).url.replace('?dl=0', '?raw=1')
