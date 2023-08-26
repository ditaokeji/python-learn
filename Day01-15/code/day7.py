s1 = 'hello world'
s2 = "hello world"
s3 = """
hello
world
"""
s4 = '\nhello world\n'
s5 = '\'hello world\\'
print(s1, s2, s3, s4, s5, end='')
print(type(s1))
print(type(s2))
print(s1 == s2)
print(s3)
s6 = r'\'hello, world!\''
s7 = s6*3
s8 = s6 + s7  # 字符串拼接
s9 = ""
s9 += s8
s10 = s9[0:5]
s11 = s9[6:]
s12 = s9[:5]
s13 = s9[6:11]
s14 = s9[::2]
print(s8)

# 一系列的字符串处理方法
# 1. 判断字符串是否以指定的字符串开头
print(s9.capitalize())
# 2. 判断字符串是否以指定的字符串结尾
print(s9.endswith('!'))
# 3. 查找指定字符串
print(s9.find('or'))
# 4. 获取字符串每个单词首字母大写的拷贝
print(s9.title())
# 5. 判断字符串是否是大写
print(s9.isupper())
# 6. 判断字符串是否是小写
print(s9.islower())
# 7. 判断字符串是否是空白字符
print(s9.isspace())
# 8. 判断字符串是否是数字
print(s9.isdigit())
# 9. 判断字符串是否是以数字构成的
print(s9.isalnum())
# 10. 获取字符串左右两侧的空白字符
print(s9.strip())
# 11. 获取字符串左侧的空白字符
print(s9.lstrip())
# 12. 获取字符串右侧的空白字符
print(s9.rstrip())
# 13. 将字符串以指定的宽度居中并在两侧填充指定的字符
print(s9.center(50, '*'))
# 14. 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(s9.rjust(50, ' '))

# 格式化输出字符串
a, b = 5, 10
print('%d * %d = %d' % (a, b, a*b))
print('{0} * {1} = {2}'.format(a, b, a*b))
print(f'{a} * {b} = {a*b}')

# 使用列表
li = [1, 3, 5, 7, 100]
print(li)
list2 = ['hello'] * 5
print(list2)
print(len(li))
li[0] = 2
print(li)
print(li[-1])
print(li[-3])
li.append(200)
li.insert(1, 400)
li += [1000, 2000]
print(li)
for index in range(10):
    li.append(index)

print(li)
li.remove(3)
li.insert(3, 3)
for i in range(len(li)):
    print(i)
    if li[i] == 3:
        print(i)
        # li.remove(li[i])
print(li)
li.pop(0)
li.pop(len(li)-1)

# 切片

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
for fruit in fruits:
    print(fruit.title(), end=' ')

print("------------")
print(fruits)
fruit2 = fruits[1:4]
print(fruit2)
fruit3 = fruits[:]
print(fruit3)
fruit4 = fruits[-3:-1]
print(fruit4)
fruit5 = fruits[::-1]
print(fruit5)

# 排序
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
print(list2)
list3 = sorted(list1, reverse=True)
print(list3)
list4 = sorted(list1, key=len)
print(list4)

# 生成式和生成器

f = [x for x in range(1, 10)]
print(f)
f= [x+y+z for x in 'abc' for y in '123' for z in '@#$']
print(f)

# 使用元组
t = ('骆昊', 38, True, '四川成都')
print(t)
print(t[0])
print(t[3])
for member in t:
    print(member)
t = ('王大锤', 20, True, '云南昆明')
print(t)
person = list(t)
print(person)
person[0] = '李小龙'
person[1] = 25
print(person)
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)


# 使用集合
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length = ', len(set1))
set2 = set(range(1, 10))
print(set2)
print(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set3)
set4 =set([1, 2])
print(set4)
set5 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}

# 向集合添加元素和从集合删除元素
set1.add(4)
set1.add(5)
set2.update([11, 12])
set2.discard(5)
if 4 in set2:
    set2.remove(4)
print(set1, set2)
print(set3.pop())
print(set3)


# 集合的成员、交集、并集、差集等运算
print(set1 & set2)
print(set1.intersection(set2))
print(set1 | set2)
print(set1.union(set2))
print(set1 - set2)
print(set1.difference(set2))
print(set1 ^ set2)
print(set1.symmetric_difference(set2))
print(set2 <= set1)
print(set2.issubset(set1))
print(set3 <= set1)
print(set3.issubset(set1))
print(set1 >= set2)
print(set1.issuperset(set2))
print(set1 >= set3)
print(set1.issuperset(set3))

# 使用字典
scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
print(scores)
print(scores['骆昊'])
print(scores['狄仁杰'])
for elem in scores:
    print('%s\t--->\t%d' % (elem, scores[elem]))
scores['白元芳'] = 65
scores['诸葛王朗'] = 71
scores.update(冷面=67, 方启鹤=85)
print(scores)
if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))
print(scores.get('武则天', 60))
print(scores.popitem())
print(scores.popitem())
print(scores.pop('骆昊', 100))
scores.clear()
print(scores)

# 练习1：在屏幕上显示跑马灯文字

import os
import time

def main():
  content = 'Welcome to Beijing'
  # while True :
    # 清理屏幕上的输出
    # os.system('cls')  # os.system('clear')
    # print(content)
    # 休眠200毫秒
    # time.sleep(0.2)
    # content = content[1:] + content[0]

if __name__ == '__main__':
  main()

# 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。

import random

def gen_code(code_len=4):
    chats = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    last_pos = len(chats) - 1
    code=""
    for _ in range(code_len):
       index = random.randint(0, last_pos)
       code += chats[index]
    return code
  
if __name__ == '__main__':
  print(gen_code(6))

# 练习3：设计一个函数返回给定文件名的后缀名。
  def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''