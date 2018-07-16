var http = new XMLHttpRequest();
function loadDoc() {
var prevStartDate = document.getElementById('id1').value
var prevEndDate = document.getElementById('id2').value
var currentStartDate = document.getElementById('id3').value
var currentEndDate = document.getElementById('id4').value
var params = `date1=${currentStartDate}&date2=${currentEndDate}&oldDate1=${prevStartDate}&oldDate2=${prevEndDate}`;

    var url = "http://localhost:5000/api/v1/innroad/report";
    http.open("GET", url+"?"+params, true);
    window.location.href = url+"?"+params;
}

function downloadExcel() {
    var url = "http://localhost:5000/api/v1/innroad/report/excel";
    var params = window.location.href.split('?')[1];
    http.open("GET", url+"?"+params, true);
    http.onreadystatechange = function()
    {
        if(this.readyState == 4 && this.status == 200) {
            var myObj = this.response;
           alert(myObj);
        }
    }
    http.send(null);
}

function downloadPdf() {
    var url = "http://localhost:5000/api/v1/innroad/report/pdf";
    var params = window.location.href.split('?')[1];
    http.open("GET", url+"?"+params, true);
    http.onreadystatechange = function()
    {
        if(this.readyState == 4 && this.status == 200) {
            var myObj = this.response;
            alert(myObj);
        }
    }
    http.send(null);
}