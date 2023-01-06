liczby=[]
# print(liczby)
for i in range(10):
    liczby.append(i+1)
# print(liczby)

odwrot=[]
for i in range(10):
    odwrot.append(liczby[-i+9])
# print(odwrot)




im='Nina Koscik'
im=list(im)
# print(im)

sp=[]
for i in range(len(im)):
    if im[i] != 'a' and im[i] != 'i' and im[i] != 'o':
        sp.append(im[i])
# print(sp)


dr=[]
for i in range(len(im)):
    if i % 2 == 0:
        dr.append(im[i])
print(dr)
    

