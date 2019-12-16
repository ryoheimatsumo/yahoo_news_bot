import urllib.request
from bs4 import BeautifulSoup

url = 'https://news.yahoo.co.jp/topics'
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) '\
     'AppleWebKit/537.36 (KHTML, like Gecko) '\
     'Chrome/55.0.2883.95 Safari/537.36 '

def getAllTopics():
    req = urllib.request.Request(url, headers={'User-Agent': ua})
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html, "html.parser")
    topicsindex = soup.find('div', attrs={'class': 'topicsListAllMain'})

    topics = topicsindex.find_all('li')

    news_list = []

    for topic in topics:
        a_tag = topic.find('a')
        href = a_tag.attrs['href']
        title = a_tag.contents[0]
        news_list.append(title)
        news_list.append(href)

    result = '\n'.join(news_list)
    return result

def getNews(word):
    req = urllib.request.Request(url, headers={'User-Agent': ua})
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html, "html.parser")
    main = soup.find('div', attrs={'class': 'topicsListAllMain'})
    topics = main.select("li > a")

    count = 0
    list = []

    for topic in topics:
        if topic.contents[0].find(word) > -1:
            list.append(topic.contents[0])
            list.append(topic.get('href'))
            count += 1
    if count == 0:
        list.append("記事が見つかりませんでした！！")

    result = '\n'.join(list)
    return result
