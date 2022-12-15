class CorruptedSaveFileError(Exception):

    def __init__(self, message):
        super(CorruptedSaveFileError, self).__init__(message)