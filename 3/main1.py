f = open('input', 'r').read().splitlines()
f = [['.'] + [*x] + ['.'] for x in f]
f = [['.'] * len(f[0])] + f + [['.'] * len(f[0])]


def is_part(w, k):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if(f[w + i][k + j] != '.' and not f[w + i][k + j].isdigit()):
                return True
    return False

res = 0
for i in range(1, len(f) - 1):
    razem = 0
    poz = 0
    ok = False
    for j in range(len(f[i]) - 1, -1, -1):
        if(f[i][j].isdigit() and is_part(i, j)):
            ok = True
        if(f[i][j].isdigit()):
            razem += int(f[i][j]) * 10**poz
            poz += 1
        else:
            if(ok):
                res += razem
            razem = 0
            poz = 0
            ok = False

print(res)