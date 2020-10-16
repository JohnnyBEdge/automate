board={
    'topL': '',
    'topM': '',
    'topR': '',
    'midL': '',
    'midM': '',
    'midR': '',
    'lowL': 'X',
    'lowM': 'X',
    'lowR': 'X',
}
winner = ''
turn = 'x'

def printBoard(board):
    print(board['topL'] + '|' + board['topM'] + '|' + board['topR'])
    print('-+-+-')
    print(board['midL'] + '|' + board['midM'] + '|' + board['midR'])
    print('-+-+-')
    print(board['lowL'] + '|' + board['lowM'] + '|' + board['lowR'])

def checkWinner(board):
    if board['topL'] == board['topM'] == board['topR']:
       winner = board['topL']
    elif board['midL'] == board['midM'] == board['midR']:
        winner = board['midL']:
        winner = board['lowL']
    elif board['topL'] == board['midM'] == board['lowR']:
        winner = board['topL']
    elif board['topR'] == board['midM'] == board['lowL']:
        winner = board['topR']

for i in range(9):
    print(f'Turn for {turn}. Where would you like to go?')
    move = input()
    board[move] = turn
    checkWinner(board)
    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'
printBoard(board)



