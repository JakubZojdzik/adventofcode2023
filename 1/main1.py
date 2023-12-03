f = open('input', 'r').read().splitlines()

res = 0
for l in f:
    a = 0
    b = 0
    for x in l:
        if(x.isdigit()):
            a = int(x)
            break
    for x in l:
        if(x.isdigit()):
            b = int(x)
    res += 10*a+b
    print(10*a+b)

print(res)