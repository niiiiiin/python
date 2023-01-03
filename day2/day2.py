liczby=[]
# print(liczby)
for i in range(10):
    liczby.append(i+1)
    if (i+1)%2==1:
        liczby[i] = liczby[i]*2
# print(liczby)
temp = 0
for i in range(10):
    temp = temp+liczby[i]
    # print(temp)


a=[]
b=[]
for i in range(10):
    a.append(i+1)
    b.append(i+11)
# print(a,b)
c=[]
for i in range(10):
    c.append(a[i]+b[i])
# print(c)


x=[]
y=[]
for i in range(10):
    x.append(i+1)
    y.append(i+1)
for i in range(10):
    for j in range(10):
        print(x[i]*y[j], end=' ')
    print()
    