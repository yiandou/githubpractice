import random
def playGame():
    rps = ['rock', 'paper', 'scissors']
    player = input('Enter rock, paper, or scissors: ')
    if player not in rps:
        raise Exception('Invalid input')
    computer = random.choice(rps)
    problems = [{'problem': '1*2+(4/2)', 'answer': 4},{"problem": "0b101 & 0b110(Start answer with 0b)", "answer": 0b100}, {"problem": "What memory address is the BIOS stored at?(Start it with 0x)", "answer": 0xFFF0}, 
                {"problem": "What is the hexadecimal representation of the binary number 1101?(Start answer with 0x)", "answer": 0xD}, {"problem": "What is the decimal representation of the hexadecimal number 0x1A?", "answer": 26}, 
                {"problem": "What is the interrupt does the BIOS call after POST?(Start answer with 0x)", "answer": 0x19}]
    problem = random.choice(problems)
    answer = input(f"Please solve the following problem: {problem['problem']}: ")
    if problem == problems[2] or problem == problems[3] or problem == problems[5]:
        answer = int(answer, 16)
    else:
        answer = int(answer)
    if answer != problem['answer']:
        raise Exception('Incorrect answer')
    else:
        print(f'Computer: {computer}')
        if player == computer:
            print('Tie')
        elif player == 'rock' and computer == 'scissors':
            print('Player wins')
        elif player == 'paper' and computer == 'rock':
            print('Player wins')
        elif player == 'scissors' and computer == 'paper':
            print('Player wins')
        else:
            print('Computer wins')

playGame()
