import subprocess
import os
import time
from colorama import Fore, Style
from tqdm import tqdm  # For progress bar

# JS PATHS
scripts = {
    "1": {
        "name": "LayerEdge Auto Referrals",
        "path": os.path.join("autoreff", "dist", "index.js")
    },
    "2": {
        "name": "LayerEdge Autorun",
        "path": os.path.join("autorun", "main.js")
    }
}

# Function to show a progress bar while a command runs
def run_command_with_progress(command, description, project_dir):
    print(f"\n🚀 {description} is starting...\n")
    
    # Simulating progress (since subprocess doesn't show real-time output)
    with tqdm(total=100, bar_format="{l_bar}%s{bar}%s" % (Fore.YELLOW, Style.RESET_ALL)) as pbar:
        process = subprocess.Popen(command, shell=True, cwd=project_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while process.poll() is None:  # While process is still running
            time.sleep(0.3)  # Simulate work
            pbar.update(10)  # Update progress
        pbar.update(100 - pbar.n)  # Complete the progress bar
    
    if process.returncode == 0:
        print(f"\n✅ {description} completed successfully!\n")
    else:
        print(f"\n❌ Error: {description} failed!\n")

# Display Menu
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

# User input
choice = input("\nSelect Number To Start: ")

if choice == "3":
    # Run npm install & build for "autoreff"
    run_command_with_progress("npm install", "Installing dependencies for autoreff", "autoreff")
    run_command_with_progress("npm run build", "Building autoreff", "autoreff")
    # Run npm install for "autorun"
    run_command_with_progress("npm install", "Installing dependencies for autorun", "autorun")
elif choice in scripts:
    script_path = scripts[choice]["path"]
    if os.path.exists(script_path):
        print(f"\nRunning {scripts[choice]['name']}...\n")
        # Using full path for node to avoid REPL
        subprocess.run(["/usr/bin/node", script_path], shell=False)  # Start JS files
    else:
        print(f"\n❌ Error: Script file not found at {script_path}")
else:
    print("\n❌ Invalid choice! Please enter a valid number.")
