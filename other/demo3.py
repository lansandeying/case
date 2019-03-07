import time 
from tomorrow import threads
from selenium import webdriver
import requests

list=[
            'https://pypi.org/project/tomorrow/0.2.0/',
            'https://www.cnblogs.com/pyld/p/4716744.html',
            'http://www.xicidaili.com/nn/10',
            'http://baidu.com',
            'http://www.bubuko.com/infodetail-1028793.html?yyue=a21bo.50862.201879',
        ] 
@threads(10)  
def     download(url):

        return requests.get(url)

def testBaidu1():
    start = time.time()
    for i in list:           
        download(i)
    end=time.time()
    print("Time: %f seconds" % (end - start))

if __name__=="__main__":
    testBaidu1()
    