from Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP1 = "127.0.0.1"
PORT1 = 8080
IP2 = "127.0.0.1"
PORT2 = 8081

# -- Create a client object
c1 = Client(IP1, PORT1)
c2 = Client(IP2, PORT2)


gene = "../S04/sequences/FRAT1.txt"
s = Seq()
s.read_fasta(gene)
sequence = s.strbases

print(f"Gene FRAT1:{sequence}")
print(f"Sending the FRAT1 Gene to the server,in fragments of 10 bases...")


for i in range(10):

    fragment = sequence[10*i : 10*i+10]
    print(f"Fragment {i + 1}: {fragment}")

    if (i + 1) % 2 != 0:
        response = c1.talk(f"Fragment {i + 1}: {fragment}")
    else:
        response = c2.talk(f"Fragment {i + 1}: {fragment}")