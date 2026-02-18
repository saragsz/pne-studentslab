from pathlib import Path

FILENAME = "sequences/ADA.txt"
file_contents = Path(FILENAME).read_text()

no_header = file_contents.split("\n")[1:]
right_text = "".join(no_header)

max_coordinate = 44652852
EXON_FILE = "ADA_EXONS.txt"
exon_contents = Path(EXON_FILE).read_text()
exons = exon_contents.split("\n")
#tengo que separar el header de cada exon con un split ">" y quitar la primera linea
print("Exon | Long. | Start  | End")
print("-----------------------------")

exon_number = 1
for exon in exons:
    if exon != "":
        position = right_text.find(exon)

        if position != -1:
            lenght = len(exon)

            start = max_coordinate - position
            end = max_coordinate - (position + lenght - 1)

            print(exon_number, "|" , lenght , "|" , start , "|", end )

        exon_number += 1