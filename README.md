# sql-inject-tool

批量检测sql注入的一些代码，暂时没有整理

使用方法：python google_url_get.py获取url，把搜索内容写入queries.txt，用换行分割，脚本会读取，并爬取前十页的url写入url.txt，再使用api_call.py自动检测sql注入，需要先开启sqlmapapi，开启命令：python3 sqlmapapi.py -s
          
