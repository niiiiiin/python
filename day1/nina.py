artur = 50
nina = 10
mila = 20
tymon = artur+nina+mila
# print(tymon)
tymon = tymon*0.5
# print(tymon)
if tymon>50:
    tymon=tymon-10
else:
    tymon=tymon+20

# print(tymon)


dzieci = [artur, nina, mila, tymon]


# for d in dzieci:  
#     d=d+100
#     print(d)
# print(dzieci)

for i in range(len(dzieci)):
    dzieci[i] = dzieci[i]+100
    # print(dzieci[i])

print(dzieci)

for i in range(len(dzieci)):
    if dzieci[i]>=150:
        dzieci[i]=dzieci[i]-50

print(dzieci)
