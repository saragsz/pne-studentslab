from pathlib import Path
def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    text = file_contents.split("\n")[1:]
    final_text = "".join(text)
    return final_text

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    bases_list = ["A", "C", "T", "G"]
    d = {}
    for base in bases_list:
        d[base] = seq.count(base)
    return d

def seq_reverse(seq, n):
    return seq[:n][::-1]

def seq_complement(seq):
    replace = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    complement_seq = ""
    for base in seq:
        complement_seq += replace[base]
    return complement_seq

