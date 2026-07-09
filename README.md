# 🎮 Online Tic-Tac-Toe

<p align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&pause=1000&color=00C853&center=true&vCenter=true&width=800&lines=Online+Tic-Tac-Toe;Python+Socket+Programming;Offline+%26+Online+Version;Made+by+Srish+Ghosh">
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Socket](https://img.shields.io/badge/Socket-TCP-success?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</p>

<p align="center">
<img src="https://media.giphy.com/media/ZVik7pBtu9dNS/giphy.gif" width="600">
</p>

---

# 📖 About

Online Tic-Tac-Toe is a beginner-friendly Python project that demonstrates how to build both an **Offline** and **Online Multiplayer** Tic-Tac-Toe game.

The online version uses Python's built-in **socket** module to allow two players to play over a Local Area Network (LAN), while the offline version supports two players on the same computer and includes voice announcements and winner storage.

This project is ideal for beginners who want to learn:

- Python
- Socket Programming
- Client-Server Architecture
- Basic Networking
- CSV File Handling
- Text-to-Speech

---

# ✨ Features

✅ Offline Tic-Tac-Toe

✅ Online Multiplayer (LAN)

✅ Client-Server Architecture

✅ Voice Announcements (pyttsx3)

✅ Winner saved as CSV

✅ Lightweight

✅ Beginner Friendly

✅ Easy to Understand Code

---

# 🎯 Available Versions

## 🎮 Offline Version

Run

```bash
python "tik tak toe.py"
```

Features

- Two players on one computer
- Voice announcements
- Winner saved to `tic_tac_toe.csv`

---

## 🌐 Online Version

Run

```bash
python server.py
```

on one computer.

Run

```bash
python client.py
```

on another computer connected to the same Wi-Fi.

---

# 📂 Project Structure

```text
Online-Tik-Tac-Toe/
│── server.py
│── client.py
│── tik tak toe.py
│── requirements.txt
│── README.md
```

---

# 📋 Requirements

- Python 3.8+
- Git
- pip

---

# 📥 Install Git

## Windows

Download Git

https://git-scm.com/download/win

Verify installation

```bash
git --version
```

---

## Ubuntu / Debian

```bash
sudo apt update
sudo apt install git
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

```bash
brew install git
```

or

```bash
xcode-select --install
```

---

# 📥 Clone Repository

```bash
git clone https://github.com/developer-srish/Online-Tik-Tac-Toe.git
```

```bash
cd Online-Tik-Tac-Toe
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install pandas pyttsx3
```

---
# ▶️ Running the Project

## 🎮 Offline Version

Run the offline version using:

```bash
python "tik tak toe.py"
```

### Features

- 👥 Two players on the same computer
- 🔊 Voice announcements
- 💾 Automatically saves the winner
- 🎯 Beginner-friendly

---

## 🌐 Online Multiplayer Version

### Step 1 — Start the Server

On the host computer run:

```bash
python server.py
```

Output:

```text
Waiting for a connection...
```

---

### Step 2 — Find Your IP Address

### Windows

```bash
ipconfig
```

Example:

```text
IPv4 Address. . . . . . . . . : 192.168.1.5
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

### Step 3 — Connect the Client

On another computer connected to the same Wi-Fi:

```bash
python client.py
```

Example:

```text
Server IP: 192.168.1.5
```

The client will connect automatically.

---

# 🎮 How to Play

The board uses the following positions.

```text
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

Example

If you enter

```text
5
```

the board becomes

```text
1 | 2 | 3
--+---+--
4 | X | 6
--+---+--
7 | 8 | 9
```

The first player to make

- Three rows
- Three columns
- Three diagonally

wins the game.

---

# 🏆 Features Comparison

| Feature | Offline | Online |
|----------|:-------:|:------:|
| Two Players | ✅ | ✅ |
| LAN Multiplayer | ❌ | ✅ |
| Voice Announcement | ✅ | ❌ |
| Save Winner to CSV | ✅ | ❌ |
| Python Sockets | ❌ | ✅ |

---

# 📁 Output

## Winner CSV

After a player wins, the offline version creates:

```text
tic_tac_toe.csv
```

Example

```csv
Winner
x
```

---

# 💡 Technologies Used

- 🐍 Python
- 🌐 Socket Programming
- 📊 pandas
- 🔊 pyttsx3
- 📄 CSV Files

---

# 📚 What You'll Learn

- Python Basics
- Socket Programming
- Client-Server Communication
- Text-to-Speech
- CSV File Handling
- Game Logic
- Console Applications

---

# ⭐ Show Your Support

If you enjoyed this project or found it helpful, please consider giving it a ⭐ on GitHub.

It helps more people discover the project and motivates me to build more open-source projects.

---
# 📜 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute this project.

---

# 👨‍💻 Author

<p align="center">

## **Srish Ghosh**

Python Developer • Open Source Enthusiast • Student

GitHub:

**https://github.com/developer-srish**

</p>

---

<p align="center">

## ⭐ Don't forget to Star this Repository!

If you enjoyed this project or found it useful, please consider giving it a ⭐ on GitHub.

It helps support the project and encourages future development.

<img src="https://media.giphy.com/media/3o7TKtnuHOHHUjR38Y/giphy.gif" width="300">

### Made with ❤️ in Python By Srish Ghosh

## Happy Coding! 🚀

</p>
