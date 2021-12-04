with open('input.txt') as f:
    lines = f.readlines()
f.close()
count = 1
lines = [int(line.strip("\n")) for line in lines]
for i in range(0,len(lines)-4):
    three_sum1 = lines[i]+lines[i+1]+lines[i+2]
    three_sum2 = lines[i+1]+lines[i+2]+lines[i+3]
    if three_sum1 < three_sum2:
        count += 1
print(count)
