def xmasstree (height = 13):
    choinka='*'
    for i in range(height):
        for j in range(-i+height-1):
            print(' ', end=' ')
        for j in range(i*2+1):
            print(choinka, end=' ')
        print()
    for i in range(height-2):
        print(' ', end=' ')
    for i in range(3):
        print('|', end=' ')
    print()
# test

xmasstree(38)