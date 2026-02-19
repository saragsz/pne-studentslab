from pathlib import Path

def get_exons(filename):
    exon_contents = Path(filename).read_text()
    exons = exon_contents.split(">")[1:]
    exon_sequences = []
    for item in exons:
        lines = item.split("\n")
        seq = "".join(lines[1:]).replace("\n", "").strip()
        exon_sequences.append(seq)
    return exon_sequences

print(get_exons("ADA_EXONS.txt"))
