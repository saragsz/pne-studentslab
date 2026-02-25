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
        if self.strbases == "NULL" or self.strbases == "NONE":
            return 0
        else:
            return self.strbases.count(base)

    def count(self):
        bases_list = ["A", "C", "T", "G"]
        d = {}
        for base in bases_list:
            d[base] = self.strbases.count(base)
        return d


