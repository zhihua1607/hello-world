import io  
import os
import sys 
import requests
from bs4 import BeautifulSoup


def spiderHostAndSave4url(fileName,urlStr):
	response = requests.request('GET',urlStr)
	soup = BeautifulSoup(response.text)
	with open(fileName, 'w') as f:
		for div in soup.find_all('div'):
			if div.get('name','default') == 'list_proxy_ip':
				contents = div.contents
				div_tag = contents[1]
				mytarget = div_tag.contents
				host=mytarget[1].text.strip().lstrip().rstrip(',')
				port=mytarget[3].text.strip().lstrip().rstrip(',')
				f.write(host+':'+port+'\n')


def spiderHostAndSave(urlDict):
	for (k,v) in urlDict.items():
		spiderHostAndSave4url(k,v)

def buildUrls():
	urls = list()
	response = requests.request('GET','http://www.proxy360.cn/Region/Japan')
	soup = BeautifulSoup(response.text)
	for a in soup.find_all('a'):
		if a.get('title','title').find('的免费代理服务器') != -1:
			urls.append(a.get('href'))
	return urls

def paserUrl2Dict(basepath,urls):
	dd = dict()
	for u in urls:
		country = u.split('/').pop()
		dd[os.path.join(basepath,country) + '.txt']=u
	return dd

def mkdir(path):
    # 引入模块
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print(path+' 创建成功')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')
        return False
 
def main():
	# 定义要创建的目录
	mkpath = "c:\\python\\learn\\host"
	# 创建目录
	mkdir(mkpath)
	#获取国家文件名称和对应要爬的url
	urlDict = paserUrl2Dict(mkpath,buildUrls())
	#爬host并保存
	spiderHostAndSave(urlDict)	

if __name__=="__main__":
	main()