file = open("input.txt", "r")
input = file.readlines()

totalscore = 0

def parse_fig(fig):
    figure = ''
    if fig == 'A':
        figure = 'rock'
    elif fig == 'B':
        figure = 'paper'
    elif fig == 'C':
        figure = 'scissors'
    elif fig == 'X':
        figure = 'lose'
    elif fig == 'Y':
        figure = 'draw'
    elif fig == 'Z':
        figure = 'win'
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
    elif res == 'lose':
        score = basic_score(fig2)
    return score

def round_play(fig1, res):
    play = ''
    if res == 'draw':
        play = fig1
    elif res == 'win':
        if fig1 == 'paper':
            play = 'scissors'
        elif fig1 == 'rock':
            play = 'paper'
        else:
            play = 'rock'
    elif res == 'lose':
        if fig1 == 'paper':
            play = 'rock'
        elif fig1 == 'rock':
            play = 'scissors'
        else:
            play = 'paper'
    return play

for ronda in input:
    totalscore += calculte_score(parse_fig(ronda[0]), round_play(parse_fig(ronda[0]), parse_fig(ronda[2])), parse_fig(ronda[2]))

print(totalscore)
