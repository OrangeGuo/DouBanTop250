#encoding=utf8
import requests
from bs4 import BeautifulSoup
import webbrowser
from wox import Wox,WoxAPI

#用户写的Python类必须继承Wox类 https://github.com/qianlifeng/Wox/blob/master/PythonHome/wox.py
#这里的Wox基类做了一些工作，简化了与Wox通信的步骤。
class Main(Wox):

  def request(self,url):
    #如果用户配置了代理，那么可以在这里设置。这里的self.proxy来自Wox封装好的对象
    if self.proxy and self.proxy.get("enabled") and self.proxy.get("server"):
      proxies = {
        "http":"http://{}:{}".format(self.proxy.get("server"),self.proxy.get("port")),
        "https":"http://{}:{}".format(self.proxy.get("server"),self.proxy.get("port"))}
      return requests.get(url,proxies = proxies)
    else:
      return requests.get(url)

  #必须有一个query方法，用户执行查询的时候会自动调用query方法
  def query(self,key):
    r = self.request('https://movie.douban.com/subject_search?',params={'search_text':key,'cat':'1002'})
    bs = BeautifulSoup(r.text)
    results = []
    for i in range(2):
      title = "1"
      url = "2"
      results.append({
        "Title": title ,
        "SubTitle":title,
        "IcoPath":"img\\fun.jpg",
        "JsonRPCAction":{
          #这里除了自已定义的方法，还可以调用Wox的API。调用格式如下：Wox.xxxx方法名
          #方法名字可以从这里查阅https://github.com/qianlifeng/Wox/blob/master/Wox.Plugin/IPublicAPI.cs 直接同名方法即可
          "method": "openUrl",
          #参数必须以数组的形式传过去
          "parameters":[url],
          #是否隐藏窗口
          "dontHideAfterAction":True
        }
      })

    return results

  def openUrl(self,url):
    webbrowser.open(url)
    WoxAPI.change_query(url)

  #以下代码是必须的
  if __name__ == "__main__":
    Main()