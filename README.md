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
    <img src="https://img.shields.io/badge/Version-1.0.0-blue">
    <img src="https://img.shields.io/badge/Python-3.8.9-blue">
    <img src="https://img.shields.io/github/stars/x6h057/GhostAgent?style=social">
    <img src="https://img.shields.io/github/forks/x6h057/GhostAgent?style=social">
</p>

---

## 👻 What is GhostAgent?
GhostAgent is a malware generator that creates backdoors utilizing the **Discord platform as a C2 Server**.

## ⚙️ How does it work?
GhostAgent leverages libraries to enable an agent to act as a **Discord bot**. Attackers communicate with the bot to execute malicious commands on the target system.

## 🚀 Features
✅ Encrypted Traffic (**HTTPS**)
✅ Customizable Configuration Settings
✅ Support for Multiple Online Agents

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

