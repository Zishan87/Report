import pandas as pd
import numpy as np
import pdfkit
import jsonpickle
# https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox-0.12.5-1.msvc2015-win64.exe and set environment variable

from jinja2 import Environment, FileSystemLoader

from Services.database_manager import DatabaseManager


class ReportManager:

    def __init__(self):
        pass

    def generating_dataframe(self, date1, date2, old_date1, old_date2):
        db_conn = DatabaseManager.db_connect()
        cursor = db_conn.cursor()

        cursor.execute("SELECT * FROM pace_report WHERE report_data > %s", date1)
        data = cursor.fetchall()
        table_columns = [column[0] for column in cursor.description]

        df = pd.DataFrame(data)
        df.columns = table_columns

        return df

    def get_report(self, date1, date2, old_date1, old_date2):
        df = self.generating_dataframe(date1, date2, old_date1, old_date2)

        return jsonpickle.encode({'message': df}, unpicklable=False)

    def excel_report(self, date1, date2, old_date1, old_date2):
        df = self.generating_dataframe(date1, date2, old_date1, old_date2)
        df.to_excel('pace_report.xlsx', sheet_name='sheet1', index=False)

        return jsonpickle.encode({'message': 'excel report download completed'})

    def pdf_report(self, date1, date2, old_date1, old_date2):
        df = self.generating_dataframe(date1, date2, old_date1, old_date2)
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template('pace_report.html')

        template_vars = {'title': 'Innroad pace report',
                         'input_dataframe': df.to_html(index=False)}
        html_out = template.render(template_vars)

        pdfkit.from_string(html_out, 'pace_report.pdf', css="style.css")

        return jsonpickle.encode({'message': 'pdf report download completed'})


























from datetime import datetime
from flask import request
# df = pd.read_sql(data, db_conn)
# ReportManager().excel_report()

# ReportManager().pdf_report()


# HTML(string=html_out).write_pdf('pace_report.pdf')

# ReportManager().generating_dataframe()


# all_result = self.reading_data()
# df = pd.DataFrame(all_result)
# df.columns = all_result.keys()


    # def reading_data(self):
    #     db_conn = None
    #     cursor = None
    #
    #     try:
    #         db_conn = DatabaseManager.db_connect()
    #         cursor = db_conn.cursor()
    #         cursor.execute('SELECT * FROM pace_report')
    #         rows = cursor.fetchall()
    #
    #     finally:
    #         if cursor is not None:
    #             cursor.close()
    #         if db_conn is not None:
    #             db_conn.close()
    #
    #     return rows

import reportlab
import json

