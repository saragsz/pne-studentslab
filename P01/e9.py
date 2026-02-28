from Seq1 import Seq

print("-----| Practice 1, Exercise 9 |------")

s = Seq()
FILENAME = "../S04/sequences/U5.txt"
s.read_fasta(FILENAME)

print(f"Sequence: (Length: {s.len()}) {s}")
print(f"Bases{s.count()}")
print(f"Rev:{s.reverse()}")
print(f"Comp:{s.complement()}")