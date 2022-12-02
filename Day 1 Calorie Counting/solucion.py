file = open("input.txt", "r")
input = file.readlines()
maximo = 0
sum = 0

for line in input:
    line = line.strip('\n')
    if line != '':
        sum += int(line)
    else:
        maximo = max(maximo, sum)
        sum = 0
print(maximo)