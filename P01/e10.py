from Seq1 import Seq

print("-----| Practice 1, Exercise 10 |------")

gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for gene in gene_list:

    rute = "../S04/sequences/" + gene + ".txt"

    s = Seq()
    s.read_fasta(rute)

    counter = s.count()

    most_freq_base = ""
    max_count = 0

    for base in counter:
        if counter[base] > max_count:
            max_count = counter[base]
            most_freq_base = base

    print("Gene", gene + ":", "Most frequent Base:", most_freq_base)