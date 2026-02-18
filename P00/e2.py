from Seq0 import seq_read_fasta

doc = seq_read_fasta("../S04/sequences/U5.txt")
print("DNA file: U5.txt")
print("The first 20 bases are:",doc[0:20])
