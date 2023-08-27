#文件和异常

#读写文本文件

# def main():
#   f = open('致橡树.txt', 'r', encoding='utf-8')
#   print(f.read())
#   f.close()

# if __name__ == '__main__':
#   main()
     
    
   
   
def main():
  f = None
  try:
    f = open('致橡树.txt', 'r', encoding='utf-8')
    print(f.read())
  except FileNotFoundError:
    print('无法打开指定的文件!')
  except LookupError:
    print('指定了未知的编码!')
  except UnicodeDecodeError:
    print('读取文件时解码错误!')
  finally:
    if f:
      f.close() 


if __name__ == '__main__':
  main()
  
# with语句和上下文管理器
def main():
  try:
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
      print(f.read())
  except FileNotFoundError:
    print('无法打开指定的文件!')
  except LookupError:
    print('指定了未知的编码!')
  except UnicodeDecodeError:
    print('读取文件时解码错误!')
    
if __name__ == '__main__':
  main()
  
#读写二进制文件
def main():
  try:
    with open('guido.jpg', 'rb') as fs1:
      data = fs1.read()
      print(type(data))
    with open('吉多.jpg', 'wb') as fs2:
      fs2.write(data)
  except FileNotFoundError as e:
    print('指定的文件无法打开.')
  except IOError as e:
    print('读写文件时出现错误.')
  print('程序执行结束.')
  
if __name__ == '__main__':
  main()
  
#读写JSON文件
import json

def main():
  mydict = {
    'name': '骆昊',
    'age': 38,
    'qq': 957658,
    'friends': ['王大锤', '白元芳'],
    'cars': [
      {'brand': 'BYD', 'max_speed': 180},
      {'brand': 'Audi', 'max_speed': 280},
      {'brand': 'Benz', 'max_speed': 320}
    ]
  }
  try:
    with open('data.json', 'w', encoding='utf-8') as fs:
      json.dump(mydict, fs)
  except IOError as e:
    print(e)  
  print('保存数据完成!')
  
if __name__ == '__main__':
  main()
  
   
   
import requests
import json

def main():
  resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
  data_model = json.loads(resp.text)
  for news in data_model['newslist']:
    print(news['title'])
       
if __name__ == '__main__':
  main() 