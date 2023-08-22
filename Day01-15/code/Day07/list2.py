"""
列表常用操作
- 列表连接
- 获取长度
- 遍历列表
- 列表切片
- 列表排序
- 列表反转
- 查找元素
"""

def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']

    for fruit in fruits:
        print(fruit.title(), end=' ')
    print()

    fruits2 = fruits[1:4]
    print(fruits2)
    print(fruits)

    fruits3 = fruits[:]
    print(fruits3)

    fruits4 = fruits[-3:-1]
    print(fruits4)

    fruits5 = fruits[::-1]
    print(fruits5)

    list2 = [x * x for x in range(1, 11)]
    print(list2)

    list3 = [m + n for m in 'ABCDEFG' for n in '12345']
    print(list3)

if __name__ == '__main__':
    main()