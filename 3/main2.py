f = open('input', 'r').read().splitlines()
f = [['.'] + [*x] + ['.'] for x in f]
f = [['.'] * len(f[0])] + f + [['.'] * len(f[0])]

neighbors = []
for i in range(len(f)):
    neighbors.append([])
    for j in range(len(f[i])):
        neighbors[i].append(set())

def around(w, k, ind):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if(f[w + i][k + j] == '*'):
                neighbors[w + i][k + j].add(ind)
                return True
    return False

ind = 0
nums = [0 for _ in range(int(1e6))]
for i in range(1, len(f) - 1):
    razem = 0
    poz = 0
    for j in range(len(f[i]) - 1, -1, -1):
        if(f[i][j].isdigit()):
            around(i, j, ind)
            razem += int(f[i][j]) * 10**poz
            poz += 1
        elif(poz != 0):
            nums[ind] = razem
            ind += 1
            razem = 0
            poz = 0

res = 0
for i in range(1, len(f) - 1):
    for j in range(1, len(f[i]) - 1):
        if(len(neighbors[i][j]) == 2 and f[i][j] == '*'):
            tmp = 1
            for x in neighbors[i][j]:
                tmp *= nums[x]
            res += tmp

print(res)