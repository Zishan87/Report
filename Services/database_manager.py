import pymssql

from Services.general_configuration_manager import GeneralConfigurationManager


class DatabaseManager:

    @classmethod
    def db_connect(cls,filename='general_config.ini', section='MSSQL'):
        params = GeneralConfigurationManager.general_config(filename, section)
        conn = pymssql.connect(**params)
        return conn