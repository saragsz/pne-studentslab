from Seq1 import Seq

print("-----| Practice 1, Exercise 6 |------")

seq_list = [Seq(),Seq("ACTGA"),Seq("Invalid sequence")]

index = 0
for seq in seq_list:
    print(f"Sequence {index}: (Length: {seq.len()}) {seq}")
    print(f"Bases{seq.count()}")
    index += 1

