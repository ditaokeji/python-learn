def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya']
    max_value = min_value = fruits[0]
    for index in range(1, len(fruits)):
        if fruits[index] > max_value:
            max_value = fruits[index]
        elif fruits[index] < min_value:
            min_value = fruits[index]
    print('max: ', max_value)
    print('min: ', min_value)
    
if __name__ == '__main__':
    main()