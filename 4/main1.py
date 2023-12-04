f = open('input', 'r').read().splitlines()
res = 0
for l in f:
    s = set()
    l = l.split()
    akt = 0
    przed = True
    for i in range(2, len(l)):
        if(przed):
            s.add(l[i])
        elif(l[i] in s):
                akt = max(1, 2*akt)
        if(l[i] == '|'):
             przed = False
    res += akt

print(res)