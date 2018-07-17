# Report
script to generate excel and pdf report

## End to end flow to generate reports.

Step 1: Reading date constraint from user (Writing GET API with query string)

Step 2: As per date intervals , I retrieved records from table
and created corresponding dataframe using 'pandas' library.

Step 3: Using Pivoting rearranged the dataframe for comparative analysis.

Step 4: Added some more series to dataframe to calculate measures of analysis.
 
Step 5: To render the report in the webpage.

        a) I have created a GET API
           http://localhost:5000/api/v1/innroad/report?date1=2018-01-08&date2=2018-03-08&oldDate1=2017-01-08&oldDate2=2017-03-08
           
        b) By using HTML template (pace_report.html) with the help of 'jinja2' package, I am sinking report to render.
        
        c) Using Javascript o call the API rom browser.
        
        d) I have also provided download buttons to download as an excel or pdf report.
        

Step 6: To download the report in Excel format

        a) I have created a GET API
           http://localhost:5000/api/v1/innroad/report/excel?date1=2018-01-08&date2=2018-03-08&oldDate1=2017-01-08&oldDate2=2017-03-08
            
        b) I have used dataframe method 'to_excel' to write the report in excel sheet
        
        c) Internally 'to_excel' method uses 'openpyxl' package to write the dataframe in excel.
           So, I have installed 'openpyxl' package but no need to import it.
           
           
Step 7: To download the report in pdf format

        a) I have created a GET API
           http://localhost:5000/api/v1/innroad/report/pdf?date1=2018-01-08&date2=2018-03-08&oldDate1=2017-01-08&oldDate2=2017-03-08
           
        b) I have used HTML template (pdf_report.html) to show the pdf report.
        
        c) I have used 'jinja2' package to embed dataframe report to HTML template
        
        d) I have used 'pdfkit' package to convert HTML template to pdf report.
        
        e) Actually 'pdfkit' is a wrapper over 'wkhtmltopdf' with added functionality.
           So, we have to install 'wkhtmltopdf' from 
           https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox-0.12.5-1.msvc2015-win64.exe
           
        f) I have also provided styles to pdf as per style.css read in 'pdfkit' method 
           parameter 'css'.

## R&D

I have looked at some other libraries (reportlab, weasyprint and xhtml2pdf) as well 
to create pdf report.

In windows weasyprint asks lot of dependencies to install.
I assume pdfkit and reportlab is better option than other. Reportlab is base and powerful
library to generate pdf. I have to look at that one.

To generate excel report 'pandas' is the best option which I have used here.

## Project Structure

Code is refactored. I have defined the appropriate user defined exception. For now I don't see any model to specify.
I am also working on other ways to generate the report, once model is needed will provide that into the project.

Frontend requires more changes.

For understanding purpose:

Controllers contains report_controller.py to write Web API.

Services contains all the business logic in report_manager.py, general_configuration_manager.py 
to read configuration from general_config.ini, database_manager.py to create sql server database
connection using 'pymssql' package.

general_config.ini contains database and all other general configuration apart from technical.

exception_code_table.py contains user defined exceptions, corresponding messages and error code.
report_exception.py is the file to generate appropriate exceptions in the orm of json string.

index.html is the user input page.
pace_report.html is used to generate the report in the web browser.
pdf_report.html is used to define pdf report template.
api_call.js is a javascript file.