from bs4 import BeautifulSoup
from urllib.parse import urljoin


class UrlParse(object):

    def __init__(self):
        self.new_urls = set()
        self.img_src = set()

    # 创建一个方法获取HTML的地址
    def __get_html(self, base: str, soup: BeautifulSoup):
        arr = soup.find_all('a')
        for a in arr:
            href = a['href']
            self.new_urls.add(urljoin(base, href))
        return self.new_urls

    # 创建一个方法获取HTML的图片信息
    def __get_img(self, base: str, soup: BeautifulSoup):
        arr = soup.find_all('img')
        for img in arr:
            src = img['src']
            self.img_src.add(urljoin(base, src))
        return self.img_src

    # 编写一个方法解析传入的html代码
    def parse_html(self, base: str, html_doc: str):
        soup = BeautifulSoup(html_doc, 'html.parser')
        new_urls = self.__get_html(base, soup)
        img_src = self.__get_img(base, soup)
        return (new_urls, img_src)


if __name__ == '__main__':
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="/tillie" class="sister" id="link3">Tillie</a>;
    <img src='abc.png' />
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """

    up = UrlParse()
    new_urls, img_src = up.parse_html("http://www.163.com", html_doc)
    print(new_urls)
    print(img_src)
