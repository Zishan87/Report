from flask import Flask, request, render_template, render_template_string

from Services.report_manager import ReportManager

app = Flask(__name__)


@app.route('/')
def server_1():
    return render_template('index.html'), 200


@app.route('/api/v1/innroad/report', methods=['GET'])
def get_report():
    date1 = request.args.get('date1')
    date2 = request.args.get('date2')
    old_date1 = request.args.get('oldDate1')
    old_date2 = request.args.get('oldDate2')
    return render_template_string(ReportManager(date1, date2, old_date1, old_date2).get_report()), 200


@app.route('/api/v1/innroad/report/excel', methods=['GET'])
def download_excel_report():
    date1 = request.args.get('date1')
    date2 = request.args.get('date2')
    old_date1 = request.args.get('oldDate1')
    old_date2 = request.args.get('oldDate2')
    return ReportManager(date1, date2, old_date1, old_date2).excel_report()


@app.route('/api/v1/innroad/report/pdf', methods=['GET'])
def download_pdf_report():
    date1 = request.args.get('date1')
    date2 = request.args.get('date2')
    old_date1 = request.args.get('oldDate1')
    old_date2 = request.args.get('oldDate2')
    return ReportManager(date1, date2, old_date1, old_date2).pdf_report(), 200


if __name__ == '__main__':
    app.run(host='localhost', port='5000')
