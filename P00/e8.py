from Seq0 import seq_read_fasta, seq_count

if __name__ == "__main__":

    print("----Exercise 8----")
    gene_list = ["U5", "ADA", "FRAT1", "FXN"]

    for gene in gene_list:
        rute = "../S04/sequences/" + gene + ".txt"
        seq = seq_read_fasta(rute)
        counter = seq_count(seq)

        most_freq_base = ""
        max_count = 0

        for base in counter:
            if counter[base] > max_count:
                max_count = counter[base]
                most_freq_base = base
        print("Gene", gene , ":","Most frequent base:", most_freq_base)