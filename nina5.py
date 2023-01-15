lst = 111111111
# print(ls)
def one_digit(ls):
    ls=str(ls)
    for i in range(len(ls)):
        if ls[0]!=ls[i]:
            return False
    return True

# print(one_digit(lst))

liczby = []
temp = 0
for i in range(100):
    liczby.append(i+1)
    if one_digit(liczby[i])==True:
        temp = temp + 1

# print(temp)




list1 = ['Mike', '', 'Emma', 'Kelly', '', 'Brad']

for i in range(len(list1)):
    if i < len(list1) and list1[i]=='':
        list1.pop(i)



print(list1)
