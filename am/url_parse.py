from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# features=html.parser 配置解析器
soup = BeautifulSoup(html_doc, 'html.parser')
# 直接获取某个HTML标题
print(soup.title)
# <title>The Dormouse's story</title>
# 获取标签名称
print(soup.title.name)
# u'title'
# 获取标签里面的值
print(soup.title.string)
# u'The Dormouse's story'
# 获取唯一的父标签的名称
print(soup.title.parent.name)
# u'head'
# 只能获取第一个p标签
print(soup.p)
# <p class="title"><b>The Dormouse's story</b></p>
# [] 可以获取标签的属性 <a href="">  <img src="" />
print(soup.p['class'])
# u'title'

soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
# find_all 获取所有的a标签
print(soup.find_all('a'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
if __name__ == "__main__":
    l = soup.find_all('a')
    for a in l:
        print(a['href'])
