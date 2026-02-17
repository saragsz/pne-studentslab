from pathlib import Path

FILENAME = "sequences/U5.txt"
file_contents = Path(FILENAME).read_text()

header = file_contents.split("\n")[1:]
text = "\n".join(header)
print(text)