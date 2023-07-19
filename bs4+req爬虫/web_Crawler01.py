#抓取PTT电影版面的源码（HTML）没有Cookie

import bs4
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"
#建立一个Request物件，附加 Request Headers 的信息
request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
})


#放入Request，抓取资料
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
print(data)
#解析源码，获取文章标题
root = bs4.BeautifulSoup(data, "html.parser")  #使用BeautifulSoup帮助解析HTML源码
titles = root.find_all("div", class_="title") #寻找 所有 class="title" 的div 标签
for title in titles:
    if title.a != None:
        print(title.a.string) #如果有a标签就打印