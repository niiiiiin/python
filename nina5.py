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



# print(list1)


# sortowanie

ls = [2, 7, 9, 15, 24, 5]
temp = 0
for i in range(len(ls)):
    for j in range(i, len(ls)):
        if ls[i]>ls[j]:
            temp = ls[j]
            ls[j] = ls[i]
            ls[i] = temp


# print(ls)

# wczytywanie i zmiana pliku

f = open("data.txt", "r")
# print(f.read())

lista = []

for i in f:
    lista.append(i)



for i in range(len(lista)):
    lista[i] = lista[i].strip("\n")

lista.append("wino")
lista.append("kwiaty")
lista.append("mydlo")
lista.append("jajka")

# lista = str(lista)
# print(lista)


f = open("data.txt", "w")
for i in range(len(lista)):
    f.write(lista[i]+"\n")
f.close()


f = open("data.txt", "r")
print(f.read())
