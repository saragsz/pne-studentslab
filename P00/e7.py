from Seq0 import seq_complement,seq_read_fasta

if __name__ == "__main__":
    print("----Exercise 7----")

    gene = "U5"
    rute = "../S04/sequences/" + gene + ".txt"
    seq = seq_read_fasta(rute)
    frag = seq[:20]

    print("Gene", gene)
    print("Fragment:", frag)
    print("Comp:", seq_complement(frag))