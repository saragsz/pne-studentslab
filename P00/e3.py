from Seq0 import seq_read_fasta, seq_len

if __name__ == "__main__":
    gene_list = ["U5", "ADA", "FRAT1", "FXN"]

    for gene in gene_list:
        ruta = "../S04/sequences/" + gene + ".txt"
        g = seq_read_fasta(ruta)

        print(gene, "Length:", seq_len(g))




