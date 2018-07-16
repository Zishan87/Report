import pandas as pd
import numpy as np
import pdfkit
import jsonpickle

from jinja2 import Environment, FileSystemLoader

from Services.database_manager import DatabaseManager


class ReportManager:

    def __init__(self, date1, date2, old_date1, old_date2):
        self.date1 = date1
        self.date2 = date2
        self.old_date1 = old_date1
        self.old_date2 = old_date2

    def generating_dataframe(self):
        db_conn = DatabaseManager.db_connect()
        cursor = db_conn.cursor()

        cursor.execute("SELECT *,YEAR(report_date) as year, DAY(report_date) as day FROM pace_report WHERE report_date > %s and report_date <= %s \
        or report_date > %s and report_date <= %s order by report_date",
                       (self.date1, self.date2, self.old_date1, self.old_date2))
        data = cursor.fetchall()
        table_columns = [column[0] for column in cursor.description]

        df = pd.DataFrame(data)

        df.columns = table_columns

        table = df.pivot(index='day', columns='year', values=['report_date', 'sold', 'occupancy', 'earned'])

        table['sold_difference'] = pd.Series(table[('sold', 2018)]-table[('sold', 2017)], index=table.index)
        occupancy_variance = ((table[('occupancy', 2018)] - table[('occupancy', 2017)]) / table[('occupancy', 2017)])*100
        table['%occupancy_variance'] = pd.Series(occupancy_variance, index=table.index)

        return table

    def report_in_html(self, template_name):
        df = self.generating_dataframe()
        env = Environment(loader=FileSystemLoader('./Controllers/templates'))
        template = env.get_template(template_name)

        template_vars = {'title': 'Innroad pace report',
                         'input_dataframe': df.to_html(index=True)}
        html_out = template.render(template_vars)
        return html_out

    def get_report(self):
        html_out = self.report_in_html('pace_report.html')
        return html_out

    def excel_report(self):
        df = self.generating_dataframe()
        df.to_excel('pace_report.xlsx', sheet_name='sheet1', index=True)

        return jsonpickle.encode({'message': 'excel report download completed'},unpicklable=False)

    def pdf_report(self):
        html_out = self.report_in_html('pdf_report.html')

        pdfkit.from_string(html_out, 'pace_report.pdf', css="style.css")

        return jsonpickle.encode({'message': 'pdf report download completed'},unpicklable=False)




































# https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox-0.12.5-1.msvc2015-win64.exe and set environment variable
# print(table, type(table), table[('report_date', 2017)])


# cursor.execute("SELECT * FROM pace_report WHERE report_data > %s and report_data <= %s order by report_data", (date1, date2))
        # data = cursor.fetchall()
        # table_columns = [column[0] for column in cursor.description]
        #
        # df1 = pd.DataFrame(data)
        # df1.columns = table_columns
        # print(df1)
        #
        # cursor.execute("SELECT * FROM pace_report WHERE report_data > %s and report_data <= %s order by report_data", (old_date1, old_date2))
        # data = cursor.fetchall()
        #
        # df2 = pd.DataFrame(data)
        # df2.columns = table_columns
        # print(df2)
        #
        # df = pd.concat([df1, df2], axis=1, sort=False, names=[df1,df2])

        # cursor.execute("SELECT *,EXTRACT(YEAR FROM report_date) as year, EXTRACT(DAY FROM report_date) as day FROM pace_report WHERE report_date > %s and report_date <= %s \
        #         or report_date > %s and report_date <= %s order by report_date",
        #                (self.date1, self.date2, self.old_date1, self.old_date2))



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

