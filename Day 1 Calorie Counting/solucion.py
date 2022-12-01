file = open("input.txt", "r")
input = file.readlines()
maximo = 0
sum = 0
maximos = []
for line in input:
    line = line.strip('\n')
    if line != '':
        sum += int(line)
    else:
        maximo = max(maximo, sum)
        maximos.append(maximo)
        sum = 0
print(sum(maximos.sort()[0..2]))