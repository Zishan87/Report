from unittest.mock import patch, MagicMock, Mock
from unittest import TestCase
from Services.report_manager import ReportManager


def get_mssql_patch(query_results):
    mock_dir_fmt = '__enter__.return_value.cursor.return_value.__enter__.return_value.{}'
    kwargs = {mock_dir_fmt.format(method): result for method, result in query_results.items()}
    return patch('pymssql.connect', autospec=True, return_value=MagicMock(**kwargs))


# print(get_mssql_patch({'fetchall.return_value': []}).__enter__)

@patch('Services.report_manager.ReportManager')
class TestApp(TestCase):

    def test_no_updates(self, anything):
        with get_mssql_patch({'fetchall.return_value': []}) as m_mssql:
            m_mssql.return_value.__enter__.return_value.cursor.return_value.__enter__.return_value.callproc.assert_has_calls(calls=[])