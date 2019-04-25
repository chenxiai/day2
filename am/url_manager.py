# url管理器,主要对待下载,已下载的url地址进行管理操作
class UrlManager(object):
    # 特殊方法,此方法在创建对象时自动被调用
    def __init__(self):
        # 待下载的url集合
        self.new_url = set()
        # 已下载的url集合
        self.old_url = set()

    # 创建一个方法,添加待下载的url地址
    def add_url(self, url):
        if url not in self.new_url and url not in self.old_url:
            self.new_url.add(url)

    # 创建一个方法,支持批量url地址添加
    def add_urls(self, urls):
        # for循环支持序列：列表、集合、元组
        for url in urls:
            self.add_url(url)

    # 创建一个方法,返回一个待下载的url地址
    def get_url(self):
        # pop() 随机返回一个数据,并且此数据会在当前集合删除
        url = self.new_url.pop()
        # 必须把当前地址添加到已下载的url集合
        self.old_url.add(url)
        return url

    # 创建一个方法,判断是否有待下载的url地址
    def has_new_url(self):
        return len(self.new_url) != 0


# 进行单元测试
if __name__ == "__main__":
    um = UrlManager()
    um.add_urls(['aa','bb','cc'])
    print('要下载地址为:', um.get_url())
    print(f'目前待下载地址{um.new_url},已下载URL{um.old_url}')