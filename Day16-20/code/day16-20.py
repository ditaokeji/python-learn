'''
Author: 黄艺 huangyi@tungee.com
Date: 2023-08-27 22:05:37
LastEditors: 黄艺 huangyi@tungee.com
LastEditTime: 2023-08-27 22:33:08
FilePath: \python-learn\Day16-20\code\day16-20.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#生成式的用法

prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

prices2 = {key: value for key, value in prices.items() if value > 100}
prices3 = {key for key, value in prices.items() if value > 100}
print(prices2)
print(prices3)

#嵌套的列表的坑
names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']

source = [(name, course) for name in names for course in courses]