Skip to content
Sign up

ZUBAIR x NAVEED-ID
/
Opensource
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
 main 
Opensource/NAVEED.py

NAVEED-ID Add files via upload
 1 contributor
274 lines (260 sloc)  145 KB

#!/usr/bin/python3
#--coding:utf-8--
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import os
import random
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import mechanize
from requests.exceptions import ConnectionError
import string
try:
    import requests
except ImportError:
    print('\ [✓] installing requests !...\')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\ [✓] installing futures !...\')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\ [✓] installing bs4 !...\')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as ahmadAXI
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\1b[1;97m' # 
M = '\33[1;31m' # 
H = '\33[1;32m' # 
K = '\1b[1;97m' # 
B = '\1b[1;97m' # 
U = '\1b[1;95m' # 
O = '\1b[1;97m' # 
N = '\1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
oks = []
cps = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

ugen=[]
for x in range(100):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
def jalan(z):
    for e in z + '\':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo ="""\33[1;97m
███████╗██╗   ██╗██████╗  █████╗ ██╗██████╗     ██╗  ██╗    ███╗   ██╗ █████╗ ██╗   ██╗███████╗███████╗██████╗ 
╚══███╔╝██║   ██║██╔══██╗██╔══██╗██║██╔══██╗    ╚██╗██╔╝    ████╗  ██║██╔══██╗██║   ██║██╔════╝██╔════╝██╔══██╗
  ███╔╝ ██║   ██║██████╔╝███████║██║██████╔╝     ╚███╔╝     ██╔██╗ ██║███████║██║   ██║█████╗  █████╗  ██║  ██║
 ███╔╝  ██║   ██║██╔══██╗██╔══██║██║██╔══██╗     ██╔██╗     ██║╚██╗██║██╔══██║╚██╗ ██╔╝██╔══╝  ██╔══╝  ██║  ██║
███████╗╚██████╔╝██████╔╝██║  ██║██║██║  ██║    ██╔╝ ██╗    ██║ ╚████║██║  ██║ ╚████╔╝ ███████╗███████╗██████╔╝
╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝    ╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚══════╝╚═════╝ 
                                                                                                               
'\3[1;97m[*] Creater  : ZUBAIR x NAVEED
'\3[1;33m[*] Version  : 0.0.9
'\3[1;35m[*] GitHub   : https://github.com/KINGFATH3R
'\3[1;91m[*] TEAM     : IGI
'\3[1;97mTurn on & off flight (airplane) mode before use   
--------------------------------------------------"""

def cek_apk(coki):
    session = requests.Session();w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\ %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\ ðŸŽ®  %sYour Active Application Details :'%(H))
        for i in range(len(game)):
            print(f"\ %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\ %s[%s!%s] Sorry, Apk ch
