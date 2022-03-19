from unicodedata import name
import random
# A simple Rock Paper Scissors game where you play the computer

# A Function to check if the player or machine wins
def checkWin(input):
    switch = {
        'rockrock' : 'Draw',
        'rockpaper' : 'Lose',
        'rockscissors' : 'Win',
        'paperpaper' : 'Draw',
        'paperrock' : 'Win',
        'paperscissors' : 'Lose',
        'scissorsscissors' : 'Draw',
        'scissorsrock' : 'Lose',
        'scissorspaper' : 'Win'
    }
    return switch.get(input)


def generateMachineChoice():
    choice = random.randrange(0,3)
    switch={
        0:'rock',
        1:'paper',
        2:'scissors'
    }
    return switch.get(choice)


def main():
    print('Input rock, paper, or scissors')
    player = input()
    machine = generateMachineChoice()
    print('The machine chose ', machine)
    combination = player + machine
    print(checkWin(combination))


if __name__ == '__main__':
    main()