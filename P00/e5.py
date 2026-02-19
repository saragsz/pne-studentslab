from Seq0 import seq_read_fasta, seq_count

if __name__ == "__main__":
    print("----Exercise 5----")
    gene_list = ["U5", "ADA", "FRAT1", "FXN"]

    for gene in gene_list:
        rute = "../S04/sequences/" + gene + ".txt"
        seq = seq_read_fasta(rute)
        counter = seq_count(seq)
        print("Gene", gene + ":", counter)