import subprocess
import os
import time
from colorama import Fore, Style
from tqdm import tqdm  #progress bar

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

# Function  progress bar
def run_command_with_progress(command, description, project_dir):
    print(f"\n🚀 {description} is starting...\n")
    
    with tqdm(total=100, bar_format="{l_bar}%s{bar}%s" % (Fore.YELLOW, Style.RESET_ALL)) as pbar:
        process = subprocess.Popen(command, shell=True, cwd=project_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while process.poll() is None:  # While process is still running
            time.sleep(0.3)  # Simulate work
            pbar.update(10)  # Update progress
        pbar.update(100 - pbar.n)  # Complete progress bar
    
    if process.returncode == 0:
        print(f"\n✅ {description} completed successfully!\n")
    else:
        print(f"\n❌ Error: {description} failed!\n")

# Function display menu
def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
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

    print("\nLayerEdge Scripts:\n")
    for key, value in scripts.items():
        print(f"{Fore.GREEN}{key}. {value['name']}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}3. Install & Build Scripts{Style.RESET_ALL}")
    print(f"{Fore.RED}4. Exit{Style.RESET_ALL}")

while True:
    show_menu()
    choice = input("\nSelect Number To Start: ")

    if choice == "3":
        # autoreff package install commands
        run_command_with_progress("npm install", "Installing dependencies for autoreff", "autoreff")
        run_command_with_progress("npm run build", "Building autoreff", "autoreff")
        # autorun package install commands
        run_command_with_progress("npm install", "Installing dependencies for autorun", "autorun")
        input("\nPress Enter to return to the menu...")  # press enter to return to menu
    elif choice in scripts:
        script_path = scripts[choice]["path"]
        if os.path.exists(script_path):
            print(f"\nRunning {scripts[choice]['name']}...\n")
            subprocess.run(["node", script_path], shell=True)  # start js files 
        else:
            print(f"\n❌ Error: Script file not found at {script_path}")
    elif choice == "4":
        print("\n👋 Exiting... Don't forgot to visit Scrypto Channel :)\n")
        break
    else:
        print("\n❌ Invalid choice! Please enter a valid number.")
