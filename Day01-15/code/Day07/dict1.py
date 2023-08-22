def main():
    scores = {'冯': 95, '元芳': 78, '仁杰': 82}
    print(scores['冯'])
    print(scores['仁杰'])
    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))
    scores['元芳'] = 65
    scores['王郎'] = 71
    scores.update(冷面=67, 启鹤=85)
    print(scores)

    if '则天' in scores:
        print(scores['则天'])
    print(scores.get('则天'))
    print(scores.get('则天', 60))
    print(scores)
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('冯', 100))
    scores.clear()
    print(scores)

if __name__ == '__main__':
    main()