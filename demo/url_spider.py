import requests

def get_domain(url):
    header={
        'Reference':'',
        'Cookie':'',
        'User-Agent':''
    }
    resp=requests.get(url,headers=header)
