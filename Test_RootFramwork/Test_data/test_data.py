#coding:utf-8
import xlrd
class test_data():
    def __init__(self,excelpath,sheetname):
        self.data=xlrd.open_workbook(excelpath)
        self.table=self.data.sheet_by_name(sheetname)
        #获取第一行作为key值
        
