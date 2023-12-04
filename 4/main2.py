import numpy as np

f = open('input', 'r').read().splitlines()
tab = np.ones(300, dtype=int)

ind = 1
for l in f:
    s = set()
    l = l.split()
    akt = 0
    przed = True
    for i in range(2, len(l)):
        if(przed):
            s.add(l[i])
        elif(l[i] in s):
                akt += 1
        if(l[i] == '|'):
             przed = False
    for i in range(ind+1, min(220, ind+1+akt)):
         tab[i] += tab[ind]
    ind += 1

print(np.sum(tab[1:ind]))