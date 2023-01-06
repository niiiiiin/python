warcaby=[]
for i in range(8):
    warcaby.append([])
    for j in range(8):
        warcaby[i].append('.')
# print(warcaby)

def pretty():
    for i in range(8):
        print(warcaby[i]) 
        print()


# warcaby[1][4]='x'

for i in range(8):
    for j in range(3):
        if (i+j)%2==0:
            warcaby[j][i]='x'

for i in range(8):
    for j in range(3):
        if (i+(-j+7))%2==0:
            warcaby[-j+7][i]='o'

def move(fromX,fromY, toX, toY):
    if (fromY+fromX)%2==0:
        if (toY+toX)%2==0:
            if abs(fromX-toX)==1:
                if abs(fromY-toY)==1:
                    old = warcaby[fromY][fromX]
                    warcaby[toY][toX]=old
                    warcaby[fromY][fromX]='.'

move(0,2, 1,3)
move(1,3, 2,4)
move(2,4, 3,5)


pretty()