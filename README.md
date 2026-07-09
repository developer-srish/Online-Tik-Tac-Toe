# 🎮 Online Tic-Tac-Toe

A simple **2-player Online Tic-Tac-Toe** game written in **Python** using the **socket** module. One player hosts the game (Server) and the other joins (Client). Players take turns over a local network (LAN).

---

## ✨ Features

- 🎲 Two-player gameplay
- 🌐 Play over a local network using sockets
- 🖥️ Terminal-based interface
- 🚀 Lightweight and beginner-friendly
- 📚 Great project for learning Python socket programming

---

## 📂 Project Structure

```text
Online-Tik-Tac-Toe/
│── server.py      # Host the game
│── client.py      # Join the game
│── README.md
```

---

## 📋 Requirements

- Python 3.8 or later
- Git (to clone the repository)

No external Python libraries are required.

---

# 📥 Install Git

## Windows

1. Download Git from:

   https://git-scm.com/download/win

2. Run the installer.

3. Keep the default installation settings.

4. Verify Git is installed:

```bash
git --version
```

Example output:

```text
git version 2.50.1.windows.1
```

---

## Ubuntu / Debian

```bash
sudo apt update
sudo apt install git
```

Verify:

```bash
git --version
```

---

## Fedora

```bash
sudo dnf install git
```

---

## Arch Linux

```bash
sudo pacman -S git
```

---

## macOS

Using Homebrew:

```bash
brew install git
```

Or install Apple's Command Line Tools:

```bash
xcode-select --install
```

Verify:

```bash
git --version
```

---

# 📥 Clone the Repository

Open Command Prompt, PowerShell, Terminal, or Git Bash and run:

```bash
git clone https://github.com/developer-srish/Online-Tik-Tac-Toe.git
```

Go into the project folder:

```bash
cd Online-Tik-Tac-Toe
```

---

# ▶️ Running the Game

## Step 1: Start the Server

On the computer that will host the game:

```bash
python server.py
```

The server will display:

```text
Waiting for a connection...
```

---

## Step 2: Find the Server IP Address

### Windows

```bash
ipconfig
```

Look for something like:

```text
IPv4 Address . . . . . : 192.168.1.5
```

---

### Linux

```bash
ip addr
```

or

```bash
ifconfig
```

---

## Step 3: Start the Client

On the second computer:

```bash
python client.py
```

Enter the server's IP address when asked.

Example:

```text
Enter Server IP: 192.168.1.5
```

---

# 🎮 How to Play

The board positions are:

```text
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

- Server plays as **X**
- Client plays as **O**
- Enter a number from **1** to **9** to place your mark.
- The first player to get three in a row wins.

---

# 🛠 Technologies Used

- Python
- Socket Programming

---

# 🤝 Contributing

Contributions are welcome!

1. Fork this repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push to GitHub.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 📝 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Srish Ghosh**

GitHub: https://github.com/developer-srish

---

⭐ If you like this project, don't forget to star the repository!
