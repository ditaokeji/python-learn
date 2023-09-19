'''
Author: 黄艺 huangyi@tungee.com
Date: 2023-09-19 22:03:58
LastEditors: 黄艺 huangyi@tungee.com
LastEditTime: 2023-09-19 22:04:04
FilePath: \python-learn\Day41-55\day42\vote\magirations\views.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from random import sample

from django.shortcuts import render


def show_index(request):
    fruits = [
        'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry',
        'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    ]
    return render(request, 'index.html', {'fruits': sample(fruits, 3)})