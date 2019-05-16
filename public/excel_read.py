#coding:utf-8
import xlrd
from public import log_out
log=log_out.logger()
class ExcelUtil():
    def __init__(self,excelPath,sheetName):
        self.data=xlrd.open_workbook(excelPath)
        self.table=self.data.sheet_by_name(sheetName)
        self.keys=self.table.row_values(0) #第一行作为字典参数名，一行一列[0]一行二列[1]
        #获取总行数
        self.rowNum=self.table.nrows
        #获取总列数
        self.colNum=self.table.ncols
    def dict_data(self):
        '''以第一行作为字典键，剩余行作为字典值，返回列表内套字典类型 '''
        if self.rowNum<=1:
            log.info(u"总行数小于等于1行，只有key值")
        else:
            r=[]
            j=1
            for i in range(self.rowNum-1):#除了第一行，剩几行外部循环几次
                i
                s={}
                values=self.table.row_values(j) #定义第二行为value的取值
                for x in range(self.colNum):
                    s[self.keys[x]]=values[x]  #key取值为第一行第一列，value取值为第二行第一列
                    #循环过后，key取值为第一行第二列，value取值为第二行第二列
                    #如果有三列，循环过后，key取值为第一行第三列，value取值为第二行第三列
                r.append(s)#将生成的字典，添加入列表r
                j+=1#保证外部循环时，value值取的是下一行对应的列
        return r
    
    def list_data(self):
        '''每一行作为一条列表，返回列表内套列表类型 '''
        if self.rowNum<=1:
            log.info(u"总行数小于等于1行，只有key值")
        else:
            total_list=[]
            for i in range(0,self.rowNum):
                list=[]
                for j in range(0,self.colNum):
                    rowX=self.table.cell(i,j).value
                    list.append(rowX)
                total_list.append(list)
        return total_list
        
    
if __name__=="__main__":
    a=ExcelUtil(excelPath=r'D:\eclipse_test_file\test1.xlsx',sheetName="Sheet1")
    print(a.dict_data())   
    print(a.list_data())  
    
    
    
    
    
    
    
    
    