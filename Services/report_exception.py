import json

from Services.exception_code_table import exception_code_table


class ReportException(Exception):
    def __init__(self,error_code):
        self.errorMessage = exception_code_table[error_code]
        self.errorCode = error_code

    def to_json(self):
        return json.dumps(self.__dict__)
