import pandas as pd
import socket
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
print('Welcome to Tic Tac Toe!')
board = ['1','2','3','4','5','6','7','8','9']
player="x"
i=0
def print_board():
   
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('--+---+--')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('--+---+--')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    
while True:
   
    print_board()
    
    pos=int(input('Enter position for ' + player + ': '))
    if board[pos-1] == 'x' or board[pos-1] == 'o':
        print('Invalid position')
        speak('Invalid position')
        player = 'o' if player == 'x' else 'x'
        
    else:
        board[pos-1] = player
       
        i=i+1
       
       
       
    if (board[0] == board[1] == board[2]) or (board[3] == board[4] == board[5]) or (board[6] == board[7] == board[8]) or (board[0] == board[3] == board[6]) or (board[1] == board[4] == board[7]) or (board[2] == board[5] == board[8]) or (board[0] == board[4] == board[8]) or (board[2] == board[4] == board[6]):
     print('Player ' + player + ' wins!')
     speak('Player ' + player + ' wins!')
     pd.DataFrame([player], columns=['Winner']).to_csv('tic_tac_toe.csv', index=False, header=False)
     print_board()
     break
    player = 'o' if player == 'x' else 'x'

    if i==9:
     print('Game over! It\'s a tie!')
     speak('Game over! It\'s a tie!')
     break
