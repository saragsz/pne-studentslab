from pathlib import Path
def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    text = file_contents.split("\n")[1:]
    final_text = "".join(text)
    return final_text