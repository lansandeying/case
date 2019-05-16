#coding:utf-8
import csv
def getCsv(file_name):#1路径和文件类型
    rows=[]
    with open(file_name,'r',encoding="utf-8") as f:#打开文件且读，三个参数
        readers=csv.reader(f) #直接读文件，一个参数
        for row in readers:  #将每一行写入列表
            rows.append(row)
        f.close()
        return rows
def writeCsv(file_name,data):
    with open(file_name,'w',encoding="utf-8",newline='') as f: #打开文件且写，四个参数
        write=csv.writer(f,dialect = ("excel"),delimiter=",")#写文件，三个参数     
        write.writerows(data) #协议一个列表
        f.close() #关闭
        


        
 
if __name__=="__main__":
    file_path=r"D:\csv4.csv"
#     data=[('selenium1','webdriver2'),('appium1','android2'),('appium1','ios2'),('selenium1','python2')]
#     writeCsv(file_name=file_path,data=data)
    print(getCsv(file_path))