import copy


akapit='Statystyki nie pozostawiają złudzeń, że co roku strażacy intensywnie pracują, ratując życie i dobytek ludzi. Nie wszystkie wyjazdy w 2022 r. dotyczyły pożarów (było ich 14 900). To także działania przy miejscowych zagrożeniach (takich interwencji było 26 723), jak wypadki lub usuwanie powalonych drzew. Fałszywych zgłoszeń było 4 017.'
temp=0
for i in range(len(akapit)):
    if akapit[i] == 'a' or akapit[i] == 'b' or akapit[i] == 'c':
        temp=temp+1
# print(temp)




def silnia(n):
    temp=1
    for i in range(n):
        temp = temp*(i+1)
    return temp

# print(silnia(20))

temp=str(silnia(20))

# print(temp)
tymcz=0

for i in range(len(temp)):
    tymcz=tymcz+1
    

# print(tymcz)


lista=[]

for i in range(5):
    lista.append(i+120)
    # if lista[i]%3==0:
        # print(lista[i])
    lista[i]=str(lista[i])
    lista[i]=list(lista[i])
    temp=[]
    for j in range(3):
        temp.append(lista[i][-j-1])
    lista[i]=list.copy(temp)

print(lista)


        
    
