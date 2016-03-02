from __future__ import with_statement # Required in 2.5
import signal
from contextlib import contextmanager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
from bs4 import Tag
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from collections import deque
import io
import urllib
import time
from threading import Timer
import thread, time, sys
import stopit



urls=deque()
cnt=0
dict={}
class TimeoutException(Exception): pass

@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException, "Timed out!"
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
def timeout():
    thread.interrupt_main()


def writetofile():
	global browser
	global cnt
	browser = webdriver.Firefox()
	baseurl="https://news.yahoo.com/"
	#finished=[]
	urls.append(baseurl)
	while(len(urls)>0):
		url=urls.pop()
		#try:
		#	page = urllib.urlopen(url)
		#		strin=link.get('href')
		#		if(strin and not strin in dict):
		#			dict[strin]=1
		#			print strin
		#			if((strin.startswith('http://www.theatlantic.com/politics/'))):
		#				urls.append(strin)
		#except :
		#	print "error"
	
	
	#print "x"
		try:
			with time_limit(300):
				print url
				try:
					browser.set_page_load_timeout(120)
				#browser.get(url)
					#if(not url.endswith('#disqus_thread')):
					#	url=url+'/#article-comments'
					browser.get(url)
				except:
					pass
				time.sleep(5)
				x=browser.page_source
			#print x
			#print 1
			#f=open("source"+str(cnt)+".txt","w")
			#print>>f,x
			#cnt=cnt+1
			#f.close()
				soup=BeautifulSoup(x)
				try:
					print "here"
					for link in soup.find_all('a'):
						strin=link.get('href')
						#if(not strin.endswith('#disqus_thread')):
								if(not strin.endswith('/')):
									strin=strin+'/'
								#strin=strin+'#disqus_thread'
						if(strin and not strin in dict):
							dict[strin]=1
							#print strin
							if('yahoo.com' in strin):
								#print "x"
                                                                urls.append(strin)
				except :
					print "error"
			#print 2
			#dict={}
			#page = urllib.urlopen(url)
			#soup = BeautifulSoup(page.read())
				#print "yo"
				storydiv=soup.find('div',{'class':'body yom-art-content clearfix'})
				#print storydiv
				story=""
				#print len(storydiv.find_all('p'))
				for para in storydiv.find_all('p'):
					story=story+para.text
	#x=soup.find_all('p',{'class','comment-text'})
	#x=soup.select('article[class="comment"] > p[class="comment-text"]')
			#print story

	#			fram=soup.find('iframe',{'id':'dsq-app2'})
                                button=browser.find_element_by_css_selector('button.view-comments Pt(16px) Pb(20px) W(100%) Fz(15px) C($fg-link)')
                                button.click()
	#print fram
	#			newurl=fram.get("src")
	#print newurl
	#			browser.set_page_load_timeout(120)
	#			browser.get(newurl)
				count=0
        #			time.sleep(4)
				try:
					with time_limit(60):
						print 1
						while(count<10):
	#						print 2
							count=count+1
							try:
								print 3
								#with time_limit(2):
								more=browser.find_element_by_css_selector('li.comments-button')
								more.click()
	#							print 5
								time.sleep(1)
							except:
        							print "error2"
								break
							finally:
								pass
				except:
					pass
	#print "x"	
			#print "here"
				time.sleep(1)
				x=browser.page_source
	#print x
			#print "no i wont print yo"
				soup=BeautifulSoup(x)
				x=soup.findAll('div',{'class':'text-container comments-truncate'})
	#print x
				comments=[]
	#print "y"
				for comm in x:
			#print comm
					temp="<comment>"
					for tex in comm.findAll('p'):
					#print tex.string
						temp=temp+tex.text
					temp=temp+"</comment>"
				#print temp
					comments.append(temp)
			#print "c"
				if(len(comments)>0):
					f=open("users/Anindya Bhandari/Downloads/IR/YahooNews/Comments_"+str(cnt),"w")
					for comment in comments:
						try:
							print>>f,(comment.encode('utf8')+'\n')
						#print>>f,(comment[1].encode('utf8')+'\n')
						#print>>f,("_____________")
						except:
							pass
					f.close()
					f=open("users/Anindya Bhandari/Downloads/IR/YahooNews/Article_"+str(cnt),"w")
					print>>f,(story.encode('utf8')+'\n')
					cnt=cnt+1;
	#for part in story:
	#	print>>f,(part.string.encode('utf8')+'\n')
					f.close()
		except Exception as e:
			print "Timed out!"
			print e.message
		#try:
		#	browser.quit()
		#except:
		#	pass
		#	browser = webdriver.Firefox()	
	#writetofile()
	return


# now Firefox will run in a virtual display. 
# you will not see the browser.
if __name__=='__main__':
	#display = Display(visible=0, size=(800, 600))
	#display.start()
	#global browser
	#browser = webdriver.Firefox()
	#baseurl="http://zeenews.india.com/news"
	#finished=[]
	#urls.append(baseurl)
	writetofile()
	#maxcount=50
	#count=0
	#while((len(urls)>0)and(count<=maxcount)):
	#	url=urls.pop()
	#	try:
	#		page = urllib.urlopen(url)
	#		soup = BeautifulSoup(page.read())
	#		print count
	#		for link in soup.find_all('a'):
	#			strin=link.get('href')
	#			if(strin and not strin in dict):
	#				dict[strin]=1
	#				if(strin.startswith(baseurl) and (('http://www.ndtv.com/india-news/' in strin))):
	#					urls.append(strin)
	#					finished.append(strin)
	#	except:
	#		print "error"
#print finished
	#cnt=0
	#print finished
	#finished=["http://www.telegraph.co.uk/finance/economics/12138466/when-is-the-next-financial-crash-coming-oil-prices-markets-recession.html#disqus_thread"]
	#for url in finished:
	#	cnt=cnt+1
	#	print cnt
	#	print url
	#	try:
	#		with time_limit(60):
	#			writetofile(url,cnt)
	#	except:
	#		print "Timed out!"
	#		try:
	#			browser.quit()
	#		except:
	#			pass
	#		browser = webdriver.Firefox()
	browser.quit()
	#display.stop()
