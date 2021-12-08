with open('input.txt') as f:
    lines = f.readlines()
f.close()
lines = [line.strip("\n") for line in lines]
gamma_rate = ""
epsilon_rate = ""
count_1 = 0
count_0 = 0
for i in range(12):
    for j in range(len(lines)):
        if lines[j][i] == '1':
            count_1+=1
        else:
            count_0+=1
    if count_0 < count_1:
        gamma_rate = gamma_rate + '1'
        epsilon_rate = epsilon_rate + '0'
    else:
        gamma_rate = gamma_rate + '0'
        epsilon_rate = epsilon_rate + '1'
    count_1 = 0
    count_0 = 0
gamma_rate = int(gamma_rate,2)
epsilon_rate = int(epsilon_rate,2)
print(epsilon_rate*gamma_rate)

