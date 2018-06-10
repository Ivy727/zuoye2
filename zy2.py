def web():
	import requests
	one=('http://www.17k.com/gexing/','http://www.17k.com/man/')  
	header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
	for i in range(2):
		url=one[i]
		response=requests.get(url,headers=header,allow_redirects=True)
		file='C://Users//admin//Desktop//lu'+str(i)+'.html'
		with open(file,'w',encoding='utf-8')as f:
			f.write(response.text)
	print(i)
web()