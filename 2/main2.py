f = open('input', 'r').read().splitlines()
res = 0

for l in f:
    cubes = {'red': 0, 'green': 0, 'blue': 0}
    l = l.split()
    for i in range(2, len(l)):
        if(i % 2 == 0):
            cubes[l[i+1].strip(',').strip(';')] = max(cubes[l[i+1].strip(',').strip(';')], int(l[i]))
    res += cubes['red'] * cubes['green'] * cubes['blue']

print(res)
