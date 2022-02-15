import xlrd
import pytest
class OperationExcel:
    # 获取sheets信息
    def get_data(self):
        data=xlrd.open_workbook('../dataconfig/case1.xls')
        tables=data.get_sheet(0)
        print(tables)
if __name__ == '__main__':
    pytest.main()
