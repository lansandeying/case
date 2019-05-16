from os import path   
d = path.dirname(__file__)  #返回当前文件所在的目录    
parent_path = path.dirname(d)
print(parent_path)