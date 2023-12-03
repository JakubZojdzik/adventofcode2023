f = open('input', 'r').read().splitlines()
cubes = {'red': 12, 'green': 13, 'blue': 14}
res = 0

for l in f:
    l = l.split()
    ind = int(l[1][:-1])
    ok = True
    for i in range(2, len(l)):
        if(i % 2 == 0):
            if(int(l[i]) > cubes[l[i+1].strip(',').strip(';')]):
                ok = False
    if(ok):
        res += ind

print(res)



# 2479 too high