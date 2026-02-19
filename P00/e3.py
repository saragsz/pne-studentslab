from Seq0 import seq_read_fasta, seq_len

if __name__ == "__main__":
    gene_list = ["U5", "ADA", "FRAT1", "FXN"]

    for gene in gene_list:
        rute = "../S04/sequences/" + gene + ".txt"
        seq = seq_read_fasta(rute)

        print(gene, "Length:", seq_len(seq))




