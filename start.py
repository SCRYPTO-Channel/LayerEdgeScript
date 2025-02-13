import subprocess
import os
from colorama import Fore, Style, init


# JS PATHS 
scripts = {
    "1": {
        "name": "LayerEdge Auto Referrals",
        "path": r"autoreff\dist\index.js"
    },
    "2": {
        "name": "LayerEdge Autorun",
        "path": r"autorun\main.js"
    }
}

# MENU
print(f"""
{Fore.CYAN + Style.BRIGHT}

 ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ 
█       █       █   ▄  █ █  █ █  █       █       █       █
█  ▄▄▄▄▄█       █  █ █ █ █  █▄█  █    ▄  █▄     ▄█   ▄   █
█ █▄▄▄▄▄█     ▄▄█   █▄▄█▄█       █   █▄█ █ █   █ █  █ █  █
█▄▄▄▄▄  █    █  █    ▄▄  █▄     ▄█    ▄▄▄█ █   █ █  █▄█  █
 ▄▄▄▄▄█ █    █▄▄█   █  █ █ █   █ █   █     █   █ █       █
█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄█  █▄█ █▄▄▄█ █▄▄▄█     █▄▄▄█ █▄▄▄▄▄▄▄█
                 LAYEREDGE SCRIPTS
{Style.RESET_ALL}
{Fore.YELLOW}╔═════════════════════════════════════════════════════════════════╗
║  {Fore.GREEN}• YouTube Channel :  https://www.youtube.com/@SCRYPTO-Channel  {Fore.YELLOW}║
║  {Fore.GREEN}• Telegram Channel : https://t.me/SCRYPTO_Newss                {Fore.YELLOW}║
║  {Fore.GREEN}• Join us now for more scripts !!                              {Fore.YELLOW}║
╚═════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
    """)
print("\nLayerEdge Scripts :\n")
for key, value in scripts.items():
    print(f"{Fore.GREEN}{key}. {value['name']}{Style.RESET_ALL}")
# input
choice = input("\nSelect Number To Start: ")

if choice in scripts:
    script_path = scripts[choice]["path"]
    if os.path.exists(script_path):
        print(f"\nRunning {scripts[choice]['name']}...\n")
        subprocess.run(["node", script_path], shell=True)  # start js files
    else:
        print(f"\nError: Script file not found at {script_path}")
else:
    print("\nInvalid choice! Please enter 1 or 2.")
