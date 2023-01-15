st = "jestem w domu i ucze sie pythona o godzinie trzynastej piecdziesiat piec"

dct={}
for i in range(len(st)):
    if st[i] not in dct:
        dct[st[i]]=1
    else:
        dct[st[i]]=dct[st[i]]+1


dct.pop(' ')

for k, v in dct.items():
    dct[k]=dct[k]*2





print(dct)
