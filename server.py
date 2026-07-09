import socket
s=socket.socket()
board = ['1','2','3','4','5','6','7','8','9']
s.bind(("", 5000))
s.listen(1)
print("Waiting for a connection...")
conn, addr = s.accept()
print("Connection from: " + str(addr))
def print_board():
   
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('--+---+--')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('--+---+--')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
print_board()
    
while True:
   
    
    
    pos=int(input('Enter position for ' + 'x' + ': '))
    if board[pos-1] == 'x' or board[pos-1] == 'o':
        print('Invalid position')
    else:
        board[pos-1] = 'x'
        conn.send(str(pos).encode())
    if (board[0] == board[1] == board[2]) or (board[3] == board[4] == board[5]) or (board[6] == board[7] == board[8]) or (board[0] == board[3] == board[6]) or (board[1] == board[4] == board[7]) or (board[2] == board[5] == board[8]) or (board[0] == board[4] == board[8]) or (board[2] == board[4] == board[6]):
        print('Player ' + 'x' + ' wins!')
        break
    print("Waiting for other player...")
    print("Dont press anything until the other player has made their move.")
    print('Because of Clicking any button will cause the game to crash and you will have to restart the game.')
    # Receive opponent's move
    pos = int(conn.recv(1024).decode())
    board[pos-1] = "o"
    print_board()
#Made by Srish Ghosh
# github:developer-srish
'''Make sure to run the server.py file first and then run the client.py file. The server will wait for a connection from the client, and once connected, the players can take turns making their moves. The game will continue until one player wins or the game ends in a tie. Enjoy playing Tic Tac Toe!'''