import requests
from xml.etree import ElementTree
import random
import time  # added for retry delay

# Terminal color
RED = "\033[31m"
CYAN = "\033[36m"
RESET = "\033[0m"

# ===============================
# ASCII Art Header
print(RED + r"______________________________________________________________________________________________________" + RESET)
print(RED + r"/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/" + RESET)
print(RED + r"______                                   _      _____                 _     _                 " + RESET)
print(RED + r"| ___ \                                 | |    /  __ \               | |   (_)                " + RESET)
print(RED + r"| |_/ /_ _ ___ _____      _____  _ __ __| |    | /  \/ ___  _ __ ___ | |__  _ _ __   ___ _ __ " + RESET)
print(RED + r"|  __/ _` / __/ __\ \ /\ / / _ \| '__/ _` |    | |    / _ \| '_ ` _ \| '_ \| | '_ \ / _ \ '__|" + RESET)
print(RED + r"| | | (_| \__ \__ \\ V  V / (_) | | | (_| |    | \__/\ (_) | | | | | | |_) | | | | |  __/ |   " + RESET)
print(RED + r"\_|  \__,_|___/___/ \_/\_/ \___/|_|  \__,_|    \_____/\___/|_| |_| |_|_.__/|_|_| |_|\___|_|   " + RESET)
print(CYAN + r"𝕧-𝟙.𝟘" + RESET)
print(CYAN + r"𝕄𝕒𝕕𝕖 𝕓𝕪: ℙ𝕖𝕛𝕦𝟛𝕟𝕔𝕖𝕣" + RESET)
print(RED + r"______________________________________________________________________________________________________" + RESET)
print(RED + r"/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/" + RESET)
print("\n")  # space before password combination

# ===============================
# 1. Get sitemap with headers and retry
sitemap_url = "https://targetexample.com/wp-sitemap.xml"
headers = {"User-Agent": "Mozilla/5.0"}

max_retries = 3
for attempt in range(max_retries):
    try:
        response = requests.get(sitemap_url, headers=headers, timeout=10)  # added headers and timeout
        response.raise_for_status()
        break
    except requests.exceptions.RequestException as e:
        print(f"Attempt {attempt+1} failed: {e}")
        if attempt < max_retries - 1:
            time.sleep(2)  # wait before retry
        else:
            print("Failed to fetch sitemap, exiting.")
            exit()

# safely decode content
xml_content = response.content.decode('utf-8', errors='ignore')

namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

try:
    root = ElementTree.fromstring(xml_content)  # safer parse
except ElementTree.ParseError as e:
    print(f"XML Parse Error: {e}")
    exit()

# ===============================
# 2. Get All URLs with safe retry
urls = []
if root.tag.endswith('urlset'):
    urls = [url.find('ns:loc', namespaces).text for url in root.findall('ns:url', namespaces)]
elif root.tag.endswith('sitemapindex'):
    sitemap_links = [s.find('ns:loc', namespaces).text for s in root.findall('ns:sitemap', namespaces)]
    for sm in sitemap_links:
        for attempt in range(max_retries):
            try:
                r = requests.get(sm, headers=headers, timeout=10)  # headers and timeout
                r.raise_for_status()
                break
            except requests.exceptions.RequestException as e:
                print(f"Sitemap {sm} attempt {attempt+1} failed: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2)
                else:
                    print(f"Skipping sitemap {sm}")
                    r = None
        if r is None:
            continue
        try:
            sub_root = ElementTree.fromstring(r.content.decode('utf-8', errors='ignore'))
        except ElementTree.ParseError as e:
            print(f"Skipping sitemap {sm} due to XML error: {e}")
            continue
        urls.extend([u.find('ns:loc', namespaces).text for u in sub_root.findall('ns:url', namespaces)])

# ===============================
# 3. Extract words from URL with alphanumeric allowed
words = set()
for url in urls:
    parts = url.replace("https://", "").replace(".html", "").replace(".php", "").split("/")
    for part in parts:
        subparts = part.split("-")
        for w in subparts:
            # allow letters and numbers, ignore "cbt"
            if w.isalnum() and len(w) > 2 and not w.lower().startswith("cbt"):
                words.add(w.lower())

# ===============================
# 4. Variations for password combinations
symbols = ["!", "@", "#", "$", "%", "&", "?"]
numbers = ["123", "2025", "111", "007", "2024"]
extras = symbols + numbers

words_list = list(words)
random.shuffle(words_list)
# limit words to 50 for terminal safety
words_list = words_list[:50]

# ===============================
# 5. Show combination in terminal
count = 0
for w1 in words_list:
    for w2 in words_list:
        if w1 != w2:
            variations = [
                f"{w1}{w2}",
                f"{w1.capitalize()}{w2}",
                f"{w1}{w2.capitalize()}",
                f"{w1.upper()}{w2.upper()}",
                f"{w1.capitalize()}{w2.capitalize()}"
            ]
            for base in variations:
                for extra in extras:
                    print(f"{base}{extra}")
                    count += 1
                    if count % 5000 == 0:
                        print(f"# {count} combination has been displayed...")

print(f"\nTotal combination: {count}")
