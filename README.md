# 🎮 Online Tic-Tac-Toe

A simple **2-player online Tic-Tac-Toe game** written in Python using the `socket` module. One player hosts the game (Server) and the other joins (Client). Players take turns over a local network.

## ✨ Features

- 🎲 Two-player gameplay
- 🌐 Online play using Python sockets
- 🖥️ Terminal-based interface
- 🚀 Lightweight and beginner-friendly
- 📚 Great project for learning socket programming

## 📂 Project Structure

```
Online-Tik-Tac-Toe/
│── server.py      # Host the game
│── client.py      # Join the game
│── README.md
```

## 📦 Requirements

- Python 3.x

No external libraries are required.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/developer-srish/Online-Tik-Tac-Toe.git
cd Online-Tik-Tac-Toe
```

### 2. Start the server

```bash
python server.py
```

The server will wait for a player to connect.

### 3. Find the server's IP address

Windows:

```bash
ipconfig
```

Linux/macOS:

```bash
ifconfig
```

or

```bash
ip addr
```

### 4. Start the client

```bash
python client.py
```

Enter the server's IP address when prompted.

## 🎮 Gameplay

- The server plays as **X**
- The client plays as **O**
- Players take turns selecting positions from **1–9**

```
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

## 🛠️ Technologies Used

- Python
- Socket Programming

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

---

Made with ❤️ by **Srish Ghosh**
