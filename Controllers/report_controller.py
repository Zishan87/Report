from flask import Flask, request

from Services.report_manager import ReportManager

app = Flask(__name__)


@app.route('/api/v1/innroad/report', methods=['GET'])
def get_report():
    date1 = request.args.get('date1')
    date2 = request.args.get('date2')
    old_date1 = request.args.get('oldDate1')
    old_date2 = request.args.get('oldDate2')
    return ReportManager().get_report(date1, date2, old_date1, old_date2)


@app.route('/api/v1/innroad/report/excel', methods=['GET'])
def download_excel_report():
    date1 = request.args.get('date1')
    date2 = request.args.get('date2')
    old_date1 = request.args.get('oldDate1')
    old_date2 = request.args.get('oldDate2')
    return ReportManager().excel_report(date1, date2, old_date1, old_date2)


@app.route('/api/v1/innroad/report/pdf', methods=['GET'])
def download_pdf_report():
    date1 = request.args.get('date1')
    date2 = request.args.get('date2')
    old_date1 = request.args.get('oldDate1')
    old_date2 = request.args.get('oldDate2')
    return ReportManager().pdf_report(date1, date2, old_date1, old_date2)


if __name__ == '__main__':
    app.run(host='localhost', port='5000')
