# Report
script to generate excel and pdf report

## End to end flow to generate reports.

Step 1: Reading date constraint from user (Writing GET API with query string)

Step 2: As per date intervals for each date interval, I retrieved records from table
and created corresponding dataframe using 'pandas' library. As we have two date interval so we have two dataframe.
(For now I used only one dataframe to show the report)

Step 3: Vertically we have to merge these two dataframe in a single dataframe (Probably 
using pivoting or some other technique) 

Step 4: Using 'numpy' library we will do all report level aggregation(sum, mean, count, variance
etc) as per business.
 
Step 5: To render the report in the webpage. (For now I am showing the json output)

        a) I have created a GET API
           http://localhost:5000/api/v1/innroad/report?date1=2018-01-08&date2=2018-03-08&oldDate1=2017-01-08&oldDate2=2017-03-08
           
        b) We can use HTML template (pace_report.html) to render report.
        
        c) We can use 'jinja2' package to embed dataframe report to HTML template
        
        d) We can also provide the appropriate styles to the template
        

Step 6: To download the report in Excel format

        a) I have created a GET API
           http://localhost:5000/api/v1/innroad/report/excel?date1=2018-01-08&date2=2018-03-08&oldDate1=2017-01-08&oldDate2=2017-03-08
            
        b) I have used dataframe method 'to_excel' to write the report in excel sheet
        
        c) Internally 'to_excel' method uses 'openpyxl' package to write the dataframe in excel.
           So, I have installed 'openpyxl' package but no need to import it.
           
Step 7: To download the report in pdf format

        a) I have created a GET API
           http://localhost:5000/api/v1/innroad/report/pdf?date1=2018-01-08&date2=2018-03-08&oldDate1=2017-01-08&oldDate2=2017-03-08
           
        b) I have used HTML template (pace_report.html) to show the pdf report.
        
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

It is not the complete project structure, so ignore the incompleteness. It requires refactoring
and lot of addition.

For understanding purpose:

Controllers contains report_controller.py to write Web API.

Services contains all the business logic in report_manager.py, general_configuration_manager.py 
to read configuration from general_config.ini, database_manager.py to create sql server database
connection using 'pymssql' package.

general_config.ini contains database and all other general configuration apart from technical.

I would add Models, User defined Exception code table, host environment and more.