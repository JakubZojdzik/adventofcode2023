
f = open('input', 'r').read().splitlines()
words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

res = 0
for l in f:
    a = 0
    b = 0
    pocz = 1e18
    kon = -1
    for i in range(len(l)):
        if(l[i].isdigit()):
            a = int(l[i])
            pocz = i
            break
    for i in range(len(l)):
        if(l[i].isdigit()):
            b = int(l[i])
            kon = i

    for i in range(len(words)):
        if(l.find(words[i]) != -1):
            if(pocz > l.find(words[i])):
                pocz = l.find(words[i])
                a = i+1

    for i in range(len(words)):
        if(l.rfind(words[i]) != -1):
            if(kon < l.rfind(words[i])):
                kon = l.rfind(words[i])
                b = i+1

    res += 10*a+b

print(res)