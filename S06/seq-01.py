class Seq:
    """A class for representing sequences"""
    def __init__(self,strbases):
        self.strbases = strbases
        print("New sequence created!")# It's not good practice to print here but let's make an exception!



# Main program
# Create an object of the class Seq
s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")

print("Testing...")
