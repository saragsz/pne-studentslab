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