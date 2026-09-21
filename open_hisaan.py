from pathlib import Path

file_path = Path("name.txt") / "hisaan.txt"

with file_path.open("r", encoding="utf-8") as f:
    print(f.read())
