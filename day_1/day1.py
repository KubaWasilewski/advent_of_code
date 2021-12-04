with open('input.txt') as f:
    lines = f.readlines()
f.close()
count = 1
lines = [line.strip("\n") for line in lines]
for i in range(0,len(lines)-1):
    if lines[i] < lines[i+1]:
        count += 1
print(count)
