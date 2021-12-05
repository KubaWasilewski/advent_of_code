with open('input.txt') as f:
    lines = f.readlines()
f.close()
lines = [line.strip("\n") for line in lines]
flist = []
ulist = []
dlist = []
x = 0
y = 0
aim = 0
for item in lines:
    if item[0] == 'f':
        flist.append(item)
    elif item[0] == 'u':
        ulist.append(item)
    else:
        dlist.append(item)
for item in lines:
    if item in flist:
        x = x + int(item[-1:])
        y = y + aim * int(item[-1:])
    elif item in ulist:
        aim = aim - int(item[-1:])
    else:
        aim = aim + int(item[-1:])
print(x*y)
