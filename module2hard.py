for tek_num in range(3, 21):
    print(tek_num, '- ', end='')
    for p1 in range(1, 21):
        for i in range(1, tek_num + 1):
            if tek_num % i == 0:
                if i - p1 > p1:
                    print(p1, i - p1, sep='', end='')
    print()
