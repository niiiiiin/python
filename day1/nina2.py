tymon = 'Tymon Koscik'

# for i in range(len(tymon)):
    # print(tymon[i])

print(tymon[6:])

tymon = tymon + ' mam 12 lat'
print(tymon)

# print(tymon.find('2'))

tymon = list(tymon)
print(tymon)
tymon[18]='1'
print(tymon)
# tymon = '|'.join(tymon)
# print(tymon)
tymon = ''.join(tymon)
print(tymon)


artur = 'Artur Derechowski mam 21 lat'

artur = list(artur)

for i in range (len(artur)):
    # print(artur[i])
    if artur[i] == '1':
        artur[i] = '4'
        # print(artur)
artur = ''.join(artur)
print(artur)
