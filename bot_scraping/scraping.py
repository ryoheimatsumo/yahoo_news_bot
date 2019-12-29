import urllib.request
from bs4 import BeautifulSoup

url_topic = 'https://news.yahoo.co.jp/topics'
url_base = 'https://news.yahoo.co.jp/search/?p='


def getAllTopics():
    req = urllib.request.Request(url_topic)
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
    url = url_base + word
    req = urllib.request.Request(url)
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html, "html.parser")
    main = soup.find('div', attrs={'id': 'NSm'})
    null_flg = False
    if not main:
        null_flg = True
    else:
        topics = main.select("h2 > a")

    count = 0
    list = []
    if null_flg == False:
        for topic in topics:
            list.append(topic.contents[0])
            list.append(topic.get('href'))
            print(topic.contents[0])
            count += 1

    if count == 0:
        list.append("記事が見つかりませんでした！！")

    result = '\n'.join(list)
    return result
