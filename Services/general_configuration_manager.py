from configparser import ConfigParser
from Services.report_exception import ReportException
from Services.exception_code_table import *


class GeneralConfigurationManager:

    @staticmethod
    def general_config(filename, section):
        parser = ConfigParser()
        parser.read(filename)
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise ReportException(SECTION_NOT_FOUND)

        return db
