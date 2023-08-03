import requests
from bs4 import BeautifulSoup as BSHTML

header={
    'Cookie':'_ga_K45575FWB8=GS1.1.1690682676.5.1.1690682918.60.0.0; _gid=GA1.2.502822429.1690794394; _ga_W62NXF3JMB=GS1.1.1690878590.57.1.1690879711.0.0.0; _ga=GA1.1.1447071462.1689778446',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
for i in range(0,100):
    url=f'https://4c1990cf8aa44be0781b5404b73dce53.ctf.hacker101.com/page/{i}'
    resp=requests.get(url)
    print(url+':'+str(resp.status_code))