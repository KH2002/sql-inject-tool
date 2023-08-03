import requests
import re
from bs4 import BeautifulSoup
import urllib3

header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
proxy={
    'https': '127.0.0.1:58309',
    'http': '127.0.0.1:58309'
}
keyword="inurl:asp?id=34"
urls = []

url="https://www.google.com.hk/search?q=inurl:\"asp?id=34\""
resp=requests.get(url,headers=header,proxies=proxy)
print(resp.status_code)
urls += re.findall('href="(https?://.*?)"', resp.text)
for link in urls:
    print (link)
# urls += re.findall('href="(https?://.*?)"', resp.text)

# with open('urls.txt', 'w') as f:
#     for url in urls:
#         f.write(url + '\n')

# for page in range(0, 101, 10):
#     url = "https://www.google.com/search?q={}&start={}".format(keyword, page)
#     r = requests.get(url, headers=header,proxies=proxy)
#     # 使用正则表达式匹配所有url
#     urls += re.findall('href="(https?://.*?)"', r.text)

# # 去重
# urls = list(set(urls))

# # 将url保存到文件
