#对付使用AJAX / XHR 技术的网站
#抓取medium.com的文章列表
#由于网页改版，可能不适用了
import json
import urllib.request as req
url = "https://medium.com/_/api/home-feed"
#建立一个Request物件，附加 Request Headers 的信息
request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
})


#放入Request，抓取资料
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
#print(data)
#解析JSON 格式的资料，获取文章标题
data = data.replace("])}while(1);</x>","")
data = json.loads(data) #把原始的 JSON 资料解析成列表

#取得 JSON资料中文章的标题
posts=data["payload"]["references"]["Post"]
for key in posts:
    post=posts[key]
    print(post["title"])