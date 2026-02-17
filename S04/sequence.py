from pathlib import Path

FILENAME = "sequences/ADA.txt"
file_contents = Path(FILENAME).read_text()

header = file_contents.split("\n")[1:]
right_text = "".join(header)

print(len(right_text))