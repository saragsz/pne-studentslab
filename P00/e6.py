from Seq0 import seq_reverse,seq_read_fasta
if __name__ == "__main__":
    print("----Exercise 6----")
    gene = "U5"
    ruta = "../S04/sequences/" + gene + ".txt"
    seq = seq_read_fasta(ruta)
    n = 20
    print("Gene", gene)
    print("Fragment:", seq[:n])
    print("Reverse:", seq_reverse(seq,n))