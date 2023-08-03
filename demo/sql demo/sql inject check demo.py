import requests


urls=open('./data.txt',mode='r',encoding='utf-8').readlines()
poc="..."
headers={
    'User-Agent':''
}   
for url in urls:
    url_poc=f'{url}{poc}'
    resp=requests.get(url_poc,headers=headers,timeout=6)
    if 'vul' in resp.text:
        print(url)