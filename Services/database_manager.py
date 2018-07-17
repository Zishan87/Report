import pymssql
import psycopg2

from Services.general_configuration_manager import GeneralConfigurationManager
from Services.exception_code_table import *
from Services.report_exception import ReportException


class DatabaseManager:

    @classmethod
    def db_connect(cls, filename='general_config.ini', section='MSSQL'):
        try:
            params = GeneralConfigurationManager.general_config(filename, section)
            conn = pymssql.connect(**params)
        except ReportException as re:
            raise re
        except Exception:
            raise ReportException(SERVER_IS_DOWN)
        else:
            return conn