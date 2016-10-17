
# coding : UTF-8
import re
import urllib
import urllib2
import time

#开始的页码
begin_page=2000
#结束的页码
end_page=2050


def GetHtml(url,page):
	page=urllib.urlopen(url)
	html=page.read()
	print('donging %s page' % page)
	return html

def GetImg(html,page):
	reg=r'src="(.+?\.jpg)"'
	imgre=re.compile(reg)
	imglist=re.findall(imgre,html)
	for imgurl in imglist:
		#urllib2.request.header("Referer","http://jandan.net/ooxx")
		opener=urllib2.build_opener()
		opener.addheaders=[('User-agent','Mozilla/5.0')]
		opener.addheaders=[('Referer','http://jandan.net/ooxx')]
		response=opener.open(imgurl)

		shijianchuo="%d" % (time.time()*1000)
		name="%s.jpg" % shijianchuo
		f=open(name,'wb')
		f.write(response.read())
		f.close()

for i in xrange(begin_page,end_page+1):
	html=GetHtml("http://jandan.net/ooxx/page-%s" % i,i)
	GetImg(html,i)

print('success')