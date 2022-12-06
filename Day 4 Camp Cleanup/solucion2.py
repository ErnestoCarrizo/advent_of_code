file = open("input.txt", "r")
input = file.readlines()
pairsNotOverlap = 0
total = 0

for line in input:
    line = line.strip('\n').split(',')
    elf1 = line[0].split('-')
    elf2 = line[1].split('-')
    if (int(elf1[0]) > int(elf2[1])) or (int(elf2[0]) > int(elf1[1])):
        pairsNotOverlap += 1
    total += 1

print(total-pairsNotOverlap)