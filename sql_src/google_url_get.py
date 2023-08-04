import re
import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings()

site = ".cn"
queries = []
with open("./sql inject/sql_src/queries.txt", "r") as f:
    queries = [query.strip() for query in f.readlines()]

num = 100
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
proxy={
    'https': '127.0.0.1:58309',
    'http': '127.0.0.1:58309'
}
results = []
for query in queries:
    query = query.replace(' ', '+')

    for i in range(0,101,10):
        URL = f"https://google.com/search?q={query}&start={i}"    
        print(URL)
        resp = requests.get(URL, headers=headers,proxies=proxy ,verify=False)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, "html.parser")

            for g in soup.find_all('div'):
                anchors = g.find_all('a')
                if anchors:
                    for anchor in anchors:
                        try:
                            link = anchor.get('href')
                            if re.match(r'^/url\?q=', link):
                                link = re.sub(r'^/url\?q=', '', link)
                                link = re.sub(r'&sa=.*', '', link)
                            if link and link.find('search?q') == -1 and link.find('google.com') == -1:
                                if link.startswith("http://") or link.startswith("https://"):
                                    if link not in results:#去重
                                        results.append(link)
                        except:
                            pass

with open("./SQL_SRC/urls.txt", "w") as f:
    for result in results:
        f.write(result + "\n")
