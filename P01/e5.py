from Seq1 import Seq

print("-----| Practice 1, Exercise 5 |------")

seq_list = [Seq(),Seq("ACTGA"),Seq("Invalid sequence")]

index = 0
for seq in seq_list:
    print(f"Sequence {index}: (Length: {seq.len()}) {seq}")
    print(f"A: {seq.count_base("A")}    C: {seq.count_base("C")}    T: {seq.count_base("T")}    G: {seq.count_base("G")}")
    index += 1



