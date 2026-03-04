from Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.72"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)


gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
s = Seq()

for gene in gene_list:
    rute = "../S04/sequences/" + gene + ".txt"
    s.read_fasta(rute)
    print(f"Sending the {gene} Gene to the server...")
    response = c.talk(str(s))
    print(f"To server:{str(s)}")
    print(f"From server: {response}")

