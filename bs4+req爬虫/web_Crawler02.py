#抓取PTT八卦版面的源码（HTML）有Cookie
import bs4
import urllib.request as req

def getData(url):

    #建立一个Request物件，附加 Request Headers 的信息
    request = req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "cookie":"over18=1",
    })


    #放入Request，抓取资料
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    #解析源码，获取文章标题
    root = bs4.BeautifulSoup(data, "html.parser")  #使用BeautifulSoup帮助解析HTML源码
    titles = root.find_all("div", class_="title") #寻找 所有 class="title" 的div 标签
    for title in titles:
        if title.a != None:
            print(title.a.string) #如果有a标签就打印

    # 抓取上一页的超链接
    nextLink=root.find("a", string="‹ 上頁") #找到内容是‹ 上頁的 a标签
    return nextLink["href"]

#主程序：抓取多个网页的标题
pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count <3:

    pageURL = "https://www.ptt.cc"+getData(pageURL)
    count+=1
print(pageURL)