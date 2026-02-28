from Seq1 import Seq

print("-----| Practice 1, Exercise 8 |------")

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

#seq1
print(f"Sequence 1: (Length: {s1.len()}) {s1}")
print(f"Bases{s1.count()}")
print(f"Rev:{s1.reverse()}")
print(f"Comp:{s1.complement()}")

#seq2
print(f"Sequence 2: (Length: {s2.len()}) {s2}")
print(f"Bases{s2.count()}")
print(f"Rev:{s2.reverse()}")
print(f"Comp:{s2.complement()}")

#seq3
print(f"Sequence 3: (Length: {s3.len()}) {s3}")
print(f"Bases{s3.count()}")
print(f"Rev:{s3.reverse()}")
print(f"Comp:{s3.complement()}")