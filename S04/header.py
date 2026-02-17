from pathlib import Path

FILENAME = "sequences/RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()

header = file_contents.split("\n")[0]
print(header)


