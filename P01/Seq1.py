from pathlib import Path
class Seq:
    def __init__(self, strbases = None):
        bases = ["A", "T", "G", "C"]

        if strbases is None:
            self.strbases = "NULL"
            print("NULL sequence created")
            return

        for i in strbases:
            if i not in bases:
                self.strbases = "ERROR"
                print("INVALID sequence created")
                return

        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return len(self.strbases)

    def count_base(self, base):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return self.strbases.count(base)

    def count(self):
        bases_list = ["A", "C", "T", "G"]
        d = {}
        for base in bases_list:
            d[base] = self.strbases.count(base)
        return d

    def reverse(self):
        if self.strbases == "ERROR":
            return "ERROR"
        elif self.strbases == "NULL":
            return "NULL"
        else:
            return self.strbases[::-1]

    def complement(self):
        replace = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        complement_seq = ""
        if self.strbases == "ERROR":
            return "ERROR"
        elif self.strbases == "NULL":
            return "NULL"
        else:
            for base in self.strbases:
                complement_seq += replace[base]
            return complement_seq

    def read_fasta(self, filename):
            file_contents = Path(filename).read_text()
            text = file_contents.split("\n")[1:]
            final_text = "".join(text)
            self.strbases= final_text