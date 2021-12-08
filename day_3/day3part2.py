with open('input.txt') as f:
    lines = f.readlines()
f.close()
lines = [line.strip("\n") for line in lines]
oxygen = ""
c02 = ""
count_0 = 0
count_1 = 0
new_lines = lines.copy()
discard_list = []
for i in range(12):
    if (len(new_lines)) == 1:
        oxygen = new_lines[0]
        break
    for j in range(len(new_lines)):
        if new_lines[j][i] == '1':
            count_1 += 1
        elif new_lines[j][i] == '0':
            count_0 += 1
    if count_0 <= count_1:
        oxygen = oxygen + '1'
    else:
        oxygen = oxygen + '0'
    for k in range(len(new_lines)):
        if new_lines[k][i] != oxygen[i]:
            discard_list.append(new_lines[k])
    for item in discard_list:
        if item in new_lines:
            new_lines.remove(item)
    count_0 = 0
    count_1 = 0
new_lines = lines.copy()
discard_list = []
for i in range(12):
    if(len(new_lines)) == 1:
        c02 = new_lines[0]
        break
    for j in range(len(new_lines)):
        if new_lines[j][i] == '1':
            count_1 += 1
        elif new_lines[j][i] == '0':
            count_0 += 1
    if count_0 <= count_1:
        c02 = c02 + '0'
    else:
        c02 = c02 + '1'
    for k in range(len(new_lines)):
        if new_lines[k][i] != c02[i]:
            discard_list.append(new_lines[k])
    for item in discard_list:
        if item in new_lines:
            new_lines.remove(item)
    count_0 = 0
    count_1 = 0
oxygen = int(oxygen,2)
c02 = int(c02,2)
print(oxygen*c02)