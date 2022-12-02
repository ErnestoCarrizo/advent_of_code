file = open("input.txt", "r")
input = file.readlines()

A = 'rock'
X = A
B = 'paper'
Y = B
C = 'scissors'
Z = C
totalscore = 0

def parse_fig(fig):
    figure = 'rock'
    if fig == 'B' or fig == 'Y':
        figure = 'paper'
    elif fig == 'C' or fig == 'Z':
        figure = 'scissors'
    return figure

def basic_score(fig):
    score = 0
    if fig == 'rock':
        score = 1
    elif fig == 'paper':
        return 2
    elif fig == 'scissors':
        return 3
    return score

def calculte_score(fig1, fig2, res):
    score = 0
    if res == 'draw':
        score = 3 + basic_score(fig1)
    elif res == 'win':
        score = 6 + basic_score(fig2)
    elif res == 'loss':
        score = basic_score(fig2)
    return score

def round_res(fig1, fig2):
    result = ''
    if fig1 == fig2:
        result = 'draw'
    elif fig1 == A:
        if fig2 == Y:
            result = 'win'
        else:
            result = 'loss'
    elif fig1 == B:
        if fig2 == Z:
            result = 'win'
        else:
            result = 'loss'
    elif fig1 == C:
        if fig2 == X:
            result = 'win'
        else:
            result = 'loss'
    return result

for ronda in input:
    resul = round_res(parse_fig(ronda[0]), parse_fig(ronda[2]))
    totalscore += calculte_score(parse_fig(ronda[0]), parse_fig(ronda[2]), resul)

print(totalscore)
