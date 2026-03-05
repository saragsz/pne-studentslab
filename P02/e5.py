from Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)


gene = "../S04/sequences/FRAT1.txt"
s = Seq()
s.read_fasta(gene)
sequence = s.strbases

print(f"Gene FRAT1:{sequence}")
print(f"Sending the FRAT1 Gene to the server,in fragments of 10 bases...")


for i in range(5):

    fragment = sequence[10*i : 10*i+10]

    print(f"Fragment {i + 1}: {fragment}")

    response = c.talk(f"Fragment {i + 1}: {fragment}")

