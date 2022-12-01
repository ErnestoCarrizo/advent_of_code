file = open("input.txt", "r")
input = file.readlines()
maximo = 0
suma = 0
maximos = []
for line in input:
    line = line.strip('\n')
    if line != '':
        suma += int(line)
    else:
        maximo = max(maximo, suma)
        suma = 0
        if maximo not in maximos:
            maximos.append(maximo)

print(sum(maximos[len(maximos)-3:]))
