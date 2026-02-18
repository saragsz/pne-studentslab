from Seq0 import seq_read_fasta,seq_count_base

if __name__ == "__main__":
    bases_list = ["A","C","T","G"]
    gene_list = ["U5", "ADA", "FRAT1", "FXN"]
    for gene in gene_list:
        ruta = "../S04/sequences/" + gene + ".txt"
        seq = seq_read_fasta(ruta)
        print ("Gene", gene + ":")

        for b in bases_list:
            count = seq_count_base(seq,b)
            print("  ", b, ":", count)
