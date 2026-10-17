import os

# Apne current folder ka path dein
# for dirpath, dirnames, filenames in os.walk('.'):
#   print(f'Folder Found: {dirpath}')
#   print(f'Subfolders: {dirnames}')
#   print(f'Files: {filenames}\n')


print("Current User:", os.environ.get("USER") or os.environ.get("USERNAME"))

# print("PATH:", os.environ.get("PATH"))

try:
    load1, load5, load15 = os.getloadavg()
    print(f"CPU Load (1 min): {load1}")
    print(f"CPU Load (5 min): {load5}")
    print(f"CPU Load (15 min): {load15}")
except OSError:
    print("Use only and only on Kali Lunux or Mac os!")




stream = os.popen('dir' if os.name == 'nt' else 'ls -l')
output = stream.read()
print("Terminal Output:\n", output)


cores = os.cpu_count()
print(f"Total cores in your system is {cores}...")
