# def func(arg):
#     return res

def nin(a,b):
    return a+b

artur = 123
tymon = 152
# print(nin(artur,tymon))

def maks(a,b):
    if a>b:
        return a
    else:
        return b

# print(maks(artur,tymon))

def maks_list(ls):
    temp = -1 if isinstance(ls[0], int) else '#'
    for i in range(len(ls)):
        # if temp < ls[i]:
        #     temp = ls[i]
        temp = maks(temp,ls[i])

    return temp

# print(maks_list([1,5,8,2,10,2,9]))

artur = list('ArturDerechowski')
# print(maks_list(artur))

def min_list(ls):
    temp = 999999 if isinstance(ls[0], int) else '~'
    for i in range(len(ls)):
        if temp > ls[i]:
            temp = ls[i]
    return temp

# print(min_list([2,5,7,9,11,1,4,5,-1]))
# print(min_list(artur))

def search(st,letter):
    for i in range(len(st)):
        if st[i] == letter:
            return True
    return False

print(search(artur,'W'))


