class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        self.strbases = strbases

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


def print_seqs(seq_list):
    index = 0
    for seq in seq_list:
        print(f"Sequence {index}: (Length: {seq.len()}) {seq}")
        index += 1


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

print_seqs(seq_list)






