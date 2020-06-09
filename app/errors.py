class DbxFileNotFoundError(Exception):
    def __init__(self):
        super().__init__("Cannot delete file from Dropbox, file not found")
