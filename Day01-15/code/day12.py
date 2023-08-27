import re

#例子1：验证输入用户名和QQ号是否有效并给出对应的提示信息

def main():
  username = input('请输入用户名: ')
  qq = input('请输入QQ号: ')
  m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
  if not m1:
    print('请输入有效的用户名.')
  m2 = re.match(r'^[1-9]\d{4,11}$', qq)
  if not m2:
    print('请输入有效的QQ号.')
  if m1 and m2:
    print('你输入的信息是有效的!')
    
if __name__ == '__main__':
  main()
  
#例子2：从一段文字中提取出国内手机号码。

def main():
  pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
  sentence = '''
  重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
  不是15600998765，也是110或119，王大锤的手机号才是15600998765。
  '''
  mylist = re.findall(pattern, sentence)
  print(mylist)
  print('----------华丽的分割线----------')
  for temp in pattern.finditer(sentence):
    print(temp.group())
  print('----------华丽的分割线----------')
  m = pattern.search(sentence)
  while m:
    print(m.group())
    m = pattern.search(sentence, m.end())

if __name__ == '__main__':
  main()

#例子3：替换字符串中的不良内容
import re


def main():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)  # 你丫是*吗? 我*你大爷的. * you.


if __name__ == '__main__':
    main()