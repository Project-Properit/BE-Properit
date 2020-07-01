import dropbox
from dropbox.files import WriteMode


# from app.errors import DbxFileNotFoundError


class DropBoxAdapter:
    def __init__(self, access_token):
        self.access_token = access_token
        self.dbx = dropbox.Dropbox(self.access_token)

    def upload_file(self, doc, dbx_filepath):
        if self.check_file_existence(dbx_filepath):  # check if uploading file already exist
            # Update existing file
            self.dbx.files_upload(doc.read(), dbx_filepath, mode=WriteMode.overwrite)
            return self.dbx.sharing_list_shared_links(dbx_filepath).links[0].url.replace('?dl=0', '?raw=1')
        else:
            # Upload new file
            self.dbx.files_upload(doc.read(), dbx_filepath)
            return self.dbx.sharing_create_shared_link_with_settings(dbx_filepath).url.replace('?dl=0', '?raw=1')

    def delete_file(self, dbx_filepath):
        if self.check_file_existence(dbx_filepath):
            self.dbx.files_delete_v2(dbx_filepath)
        # else:
        #     raise DbxFileNotFoundError

    def get_download_link(self, upload_file_path):
        return self.dbx.files_get_temporary_link(upload_file_path).link

    def check_file_existence(self, upload_file_path):
        try:
            if self.dbx.files_get_metadata(upload_file_path):
                return True
        except Exception as e:
            if isinstance(e.error, dropbox.files.GetMetadataError):
                return False
            else:
                raise
