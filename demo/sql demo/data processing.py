origin_data=open('./sql url.txt',mode='read',encoding="utf-8").readlines()
set_data=set(origin_data)
f=open('./data.txt',mode='w',encoding='utf-8')
for data in origin_data:
    if data:
        f.write(data.strip(),+'\n')