USE [zishan_sample];
GO
CREATE PROCEDURE [dbo].[usp_Get_Report]
    @startDate date,
    @endDate date,
	@oldStartDate date,
	@oldEndDate date
AS
    SET NOCOUNT ON;
    SELECT *, YEAR(report_date) as year, DAY(report_date) as day
    FROM pace_report
    WHERE report_date > @startDate and report_date <= @endDate
            or report_date > @oldStartDate and report_date <= @oldEndDate order by report_date;
GO