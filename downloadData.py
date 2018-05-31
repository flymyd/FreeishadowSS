import io
import sys
import urllib.parse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
url='https://my.ishadowx.net/'
header={'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
request=urllib.request.Request(url,headers=header)
source_code=urllib.request.urlopen(request).read()
code_list=str(source_code,encoding="utf-8")
file=open('D:\data.txt','w')
file.write(code_list)
file.close()