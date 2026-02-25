import termcolor

class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        bases = ["A", "T", "G", "C"]

        for i in strbases:
            if i not in bases:
                self.strbases = "ERROR"
                print("ERROR!!")
                return

        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

def print_seqs(seq_list,color):
    index = 0
    for seq in seq_list:
        text = f"Sequence {index}: (Length: {len(seq.strbases)}) {seq}"
        termcolor.cprint(text, color)
        index += 1

def generate_seqs(pattern, number):
    seq_list = []

    for i in range(1, number + 1):
        new_pattern = pattern * i
        seq = Seq(new_pattern)
        seq_list.append(seq)

    return seq_list

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1,"blue")

print()
print("List 2:")
print_seqs(seq_list2, "yellow")