#coding:utf-8
import requests
import os
#popen返回文件对象，跟open操作一样
f = os.popen(r"ping www.baidu.com", "r")

d = f.read()#读文件
print(d)
s = d.split("\n")#切割换行
new = [x for x in s if x != '']  # 去掉空''
print(new)
print(type(d))
f.close()
url="https://cn-zjjh5-dx-v-06.acgvideo.com/upgcxcode/89/93/9189389/9189389-1-80.flv?expires=1542543600&platform=pc&ssig=AVL5Pnr6wn7COMK2JxQEzQ&oi=454143221&nfa=7VMUDqBQpI8VGBbhQ1faUQ==&dynamic=1&hfa=2042788860&hfb=Yjk5ZmZjM2M1YzY4ZjAwYTMzMTIzYmIyNWY4ODJkNWI=&trid=12b1dae78a3a4c8f93b169c7a24a2899&nfc=1"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
,'Referer':'https://www.bilibili.com/video/av5658851/?spm_id_from=333.338.b_7265636f6d6d656e645f7265706f7274.1'}
r = requests.get(url,headers=headers,stream=True) 
file_size = float(r.headers['Content-Length'])
file_size_M=file_size/1024.0/1024.0
print(r.status_code)
print(r.headers)
print("文件大小：%dM。"%file_size_M)
#coding:utf-8
import requests
url="https://cn-zjjh5-dx-v-06.acgvideo.com/upgcxcode/89/93/9189389/9189389-1-80.flv?expires=1542543600&platform=pc&ssig=AVL5Pnr6wn7COMK2JxQEzQ&oi=454143221&nfa=7VMUDqBQpI8VGBbhQ1faUQ==&dynamic=1&hfa=2042788860&hfb=Yjk5ZmZjM2M1YzY4ZjAwYTMzMTIzYmIyNWY4ODJkNWI=&trid=12b1dae78a3a4c8f93b169c7a24a2899&nfc=1"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
,'Referer':'https://www.bilibili.com/video/av5658851/?spm_id_from=333.338.b_7265636f6d6d656e645f7265706f7274.1'}
r = requests.get(url,headers=headers,stream=True) 
file_size = float(r.headers['Content-Length'])
file_size_M=file_size/1024.0/1024.0
print(r.status_code)
print(r.headers)
print("文件大小：%dM。"%file_size_M)
'''
Request URL:https://cn-zjjh5-dx-v-06.acgvideo.com/upgcxcode/89/93/9189389/9189389-1-80.flv?expires=1542543900&platform=pc&ssig=cMlI09nKXKBvyRqPai63oA&oi=454143221&nfa=7VMUDqBQpI8VGBbhQ1faUQ==&dynamic=1&hfa=2042788017&hfb=Yjk5ZmZjM2M1YzY4ZjAwYTMzMTIzYmIyNWY4ODJkNWI=&trid=cc4b55ee555b429582e197b7a06581cf&nfc=1
Request Method:GET
Status Code:200 OK
Remote Address:61.153.102.135:443
Referrer Policy:no-referrer-when-downgrade
Response Headers
view source
Accept-Ranges:bytes
Access-Control-Allow-Origin:https://www.bilibili.com
Access-Control-Expose-Headers:Content-Length, Content-Range
alt-svc:quic=":443"; ma=2592000; v="43,42,41,39,38,37,35"
Connection:keep-alive
Content-Length:17436340
Content-Type:video/x-flv
Date:Sun, 18 Nov 2018 10:26:43 GMT
ETag:"5b9b0b2f-10a0eb4"
Last-Modified:Fri, 14 Sep 2018 01:13:19 GMT
Server:openresty
X-Cache:cn-zjjh5-dx-v-06.hdslb.com Disk
Request Headers
view source
Accept:*/*
Accept-Encoding:gzip, deflate, br
Accept-Language:zh-CN,zh;q=0.9,en;q=0.8
Connection:keep-alive
Host:cn-zjjh5-dx-v-06.acgvideo.com
Origin:https://www.bilibili.com
Referer:https://www.bilibili.com/video/av5658851/?spm_id_from=333.338.b_7265636f6d6d656e645f7265706f7274.1
User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36
Query String Parameters
view source
view URL encoded
expires:1542543900
platform:pc
ssig:cMlI09nKXKBvyRqPai63oA
oi:454143221
nfa:7VMUDqBQpI8VGBbhQ1faUQ==
dynamic:1
hfa:2042788017
hfb:Yjk5ZmZjM2M1YzY4ZjAwYTMzMTIzYmIyNWY4ODJkNWI=
trid:cc4b55ee555b429582e197b7a06581cf
nfc:1
'''
