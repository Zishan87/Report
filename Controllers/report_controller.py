from flask import Flask, request, render_template, render_template_string
from flask import make_response
from reportlab.pdfgen import canvas

from Services.report_manager import ReportManager
from Services.report_exception import ReportException
from flask_restful import Resource, Api

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
    try:
        return render_template_string(ReportManager(date1, date2, old_date1, old_date2).get_report()), 200
    except ReportException as e:
        return e.to_json(), 500


@app.route('/api/v1/innroad/report/excel', methods=['GET'])
def download_excel_report():
    date1 = request.args.get('date1')
    date2 = request.args.get('date2')
    old_date1 = request.args.get('oldDate1')
    old_date2 = request.args.get('oldDate2')
    try:
        return ReportManager(date1, date2, old_date1, old_date2).excel_report()
    except ReportException as e:
        return e.to_json(), 500


@app.route('/api/v1/innroad/report/pdf', methods=['GET'])
def download_pdf_report():
    date1 = request.args.get('date1')
    date2 = request.args.get('date2')
    old_date1 = request.args.get('oldDate1')
    old_date2 = request.args.get('oldDate2')
    try:
        return ReportManager(date1, date2, old_date1, old_date2).pdf_report(), 200
    except ReportException as e:
        return e.to_json(), 500


@app.route('/pdf')
def pdf():
    import io
    output = io.BytesIO()

    p = canvas.Canvas(output)
    p.drawString(100, 100, 'Hello')
    p.showPage()
    p.save()

    pdf_out = output.getvalue()
    output.close()

    response = make_response(pdf_out)
    response.headers['Content-Disposition'] = "attachment; filename='sakulaci.pdf"
    response.mimetype = 'application/pdf'
    return response

api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"Hello":"Wold"}

api.add_resource(HelloWorld, '/hello')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
