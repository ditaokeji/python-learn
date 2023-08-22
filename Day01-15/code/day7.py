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
list = [1, 3, 5, 7, 100]
print(list)
list2 = ['hello'] * 5
print(list2)
print(len(list))
list[0] = 2
print(list)
print(list[-1])
print(list[-3])
list.append(200)
list.insert(1, 400)
list += [1000, 2000]
print(list)












