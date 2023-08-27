
from time import time
from threading import Thread

import requests

class DownloadHandler(Thread):
  def __init__(self, url):
    super().__init__()
    self._url = url
    
  def run(self):
    filename = self._url[self._url.rfind('/') + 1:]
    resp = requests.get(self._url)
    with open('./res/' + filename, 'wb') as f:
      f.write(resp.content)

def main():
  # 通过requests模块的get函数获取网络资源
  resp = requests.get(
      'http://api.tianapi.com/meinv/?key=APIKey&num=10')
  # 将服务器返回的JSON格式的数据解析为字典
  data_model = resp.json()
  print(data_model)
  for mm_dict in data_model['newslist']:
    url = mm_dict['picUrl']
    # 通过多线程的方式实现图片下载
    DownloadHandler(url).start()    
    
    
 if __name__ == '__main__':
  main()     
  
  
#基于传输层协议的套接字编程
from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

def main():
  server = socket(family=AF_INET, type=SOCK_STREAM)
  server.bind(('192.168.1.2', 6789))
  server.listen(512)
  print('服务器启动开始监听...')
  while True:
    client, addr = server.accept()
    print(str(addr) + '连接到了服务器.')
    client.send(str(datetime.now()).encode('utf-8'))
    client.close()
    
if __name__ == '__main__':
  main()
  
  
from socket import socket

def main():
  client = socket()
  client.connect(('192.168.1.2', 6789))
  print(client.recv(1024).decode('utf-8'))
  client.close()
    
    
# 多线程开启socket
from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread

def main():
  class FileTransferHandler(Thread):
    
    def __init__(self, cclient):
      super().__init__()
      self.cclient = cclient
      
    def run(self):
      my_dict = {}
      my_dict['filename'] = 'guido.jpg'
      my_dict['filedata'] = data
      json_str = dumps(my_dict)
      self.cclient.send(json_str.encode('utf-8'))
      self.cclient.close()
        
    server = socket()
    server.bind(('192.168.1.2', 5566))
    server.listen(512)
    
    with open('guido.jpg', 'rb') as f:
      data = b64encode(f.read()).decode('utf-8')
      
    while True:
      client, addr = server.accept()
      FileTransferHandler(client).start()
      
if __name__ == '__main__':
  main()  
    
    
#客户端代码

from socket import socket
from json import loads
from base64 import b64decode


def main:
  client = socket()
  client.connect(('192.168.1.2', 5566))
  in_data = bytes()
  data = client.recv(1024)
  while data:
    in_data += data
    data = client.recv(1024)
  my_dict = loads(in_data.decode('utf-8'))
  filename = my_dict['filename']
  filedata = my_dict['filedata'].encode('utf-8')
  with open('/Users/wangxiaodong/Downloads/' + filename, 'wb') as f:
    f.write(b64decode(filedata))
  print('图片已保存.')

if __name__ == '__main__':
  main()
  
  

#网络应用开发 - 发送电子邮件

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main():
  # 请自行修改下面的邮件发送者和接收者
  sender = 'abcdefg@126.com'
  receivers = ['uvwxyz@qq.com', 'uvwxyz@126.com']
  message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
  message['From'] = Header('王大锤', 'utf-8')
  message['To'] = Header('骆昊', 'utf-8')
  message['Subject'] = Header('示例代码实验邮件', 'utf-8')
  smtper = SMTP('smtp.126.com')
  # 请自行修改下面的登录口令
  smtper.login(sender, 'secretpass')
  smtper.sendmail(sender, receivers, message.as_string())
  print('邮件发送完成!')
  
if __name__ == '__main__':
  main()  

# 发送邮件-发送带附件的邮件
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import urllib
def main():
  # 创建一个带附件的邮件消息对象
  message = MIMEMultipart()
  
  # 创建文本内容
  text_content = MIMEText('附件中有本月数据请查收', 'plain', 'utf-8')
  message['Subject'] = Header('本月数据', 'utf-8')
  # 将文本内容添加到邮件消息对象中
  message.attach(text_content)
  
  # 读取文件并将文件作为附件添加到邮件消息对象中
  with open('guido.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是jpg类型:
    mime = MIMEImage(f.read())
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='guido.jpg')
    message.attach(mime)
    
  # 创建SMTP对象
  smtper = SMTP('smtp.126.com')
  sender = 'abcdefg@126.com'
  receivers = ['wfdsjalfjsdl@qq.com']
  smtper.login(sender, 'secretpass')
  smtper.sendmail(sender, receivers, message.as_string())
  smtper.quit()
  print('邮件发送完成!')
  
  
if __name__ == '__main__':
  main()        
  
  
  
#发送短信
import urllib.parse
import http.client
import json


def main():
  host = "106.ihuyi.com"
  sms_send_uri = "/webservice/sms.php?method=Submit"
  params = urllib.parse.urlencode({'account': '你自己的账号', 'password' : '你自己的密码', 'content': '您的验证码是：147258。请不要把验证码泄露给其他人。', 'mobile': '接收者的手机号', 'format':'json' })
  print(params)
  headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
  conn = http.client.HTTPConnection(host, port=80, timeout=30)
  conn.request('POST', sms_send_uri, params, headers)
  response = conn.getresponse()
  response_str = response.read()
  jsonstr = response_str.decode('utf-8')
  print(json.loads(jsonstr))
  conn.close()
  
  
if __name__ == '__main__':
    main()
     