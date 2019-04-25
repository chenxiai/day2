# 创建URL下载器
# class UrlDownLoader(object):
from urllib3.poolmanager import PoolManager
from urllib3.response import HTTPResponse
# 没有缩进,self说明它是一个函数
from urllib.parse import urljoin


class UrlDownLoader(object):

    # 由于当前方法并未访问任何属性对象,此方法可以定义类方法
    @classmethod  # 不用创建对象,采用类调用
    def down_html(cls, root_url, encoding="UTF-8"):
        # 创建下载对象
        pm = PoolManager()
        # 指定下载方式,URL地址,编码
        res: HTTPResponse = pm.request("get", root_url)
        # 如果返回http请求协议是200则代表请求正常返回
        if res.status == 200:
            return res.data.decode(encoding=encoding)
        else:
            return None


# 单元测试
if __name__ == "__main__":
    res = UrlDownLoader.down_html("http://www.163.com", "gbk")
    print(res)
    print(urljoin("http://www.163.com", "/image/index.png"))
    print(urljoin("http://www.163.com", "http://www.163.com/image/index.png"))
    print(urljoin("http://www.163.com", "http://www.baidu.com/image/index.png"))
