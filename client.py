import socket
import time
import builtins
def print(*args, delay=0.06, end="\n"):
    text = " ".join(str(arg) for arg in args)
    for char in text:
        builtins.print(char, end="", flush=True)
        time.sleep(delay)
    builtins.print(end=end, flush=True)

board = ["1","2","3","4","5","6","7","8","9"]

s = socket.socket()

ip = input("Server IP: ")
s.connect((ip, 5000))

print("Connected!")
def print_board():
   
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('--+---+--')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('--+---+--')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    
while True:

    print("Waiting for Player X...")
    print("Dont press anything until the other player has made their move.")
    print('Because of Clicking any button will cause the game to crash and you will have to restart the game.')

    # Receive X's move
    pos = int(s.recv(1024).decode())
    board[pos-1] = "x"
    print_board()
    if (board[0] == board[1] == board[2]) or (board[3] == board[4] == board[5]) or (board[6] == board[7] == board[8]) or (board[0] == board[3] == board[6]) or (board[1] == board[4] == board[7]) or (board[2] == board[5] == board[8]) or (board[0] == board[4] == board[8]) or (board[2] == board[4] == board[6]):
        print('Player ' + 'x' + ' wins!')
        break
    pos = int(input('Enter position for ' + 'o' + ': '))
    if board[pos-1] in ['x', 'o']:
        print('Invalid position')
        break
    else:
        board[pos-1] = 'o'
        s.send(str(pos).encode())


    if (board[0] == board[1] == board[2]) or (board[3] == board[4] == board[5]) or (board[6] == board[7] == board[8]) or (board[0] == board[3] == board[6]) or (board[1] == board[4] == board[7]) or (board[2] == board[5] == board[8]) or (board[0] == board[4] == board[8]) or (board[2] == board[4] == board[6]):
     print('Player ' + 'o' + ' wins!')
     break
     
    print_board()
#Made by Srish Ghosh
# github:developer-srish
#Make sure to run the client.py file after starting the server.py file. The client will connect to the server, and once connected, the players can take turns making their moves. The game will continue until one player wins or the game ends in a tie. Enjoy playing Tic Tac Toe!
