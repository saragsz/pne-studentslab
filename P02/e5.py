from Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.72"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)


gene = "FRAT1"
s = Seq()
rute = "../S04/sequences/" + gene + ".txt"
sequence = s.read_fasta(rute)
for i in range(6):
    l = sequence[10 * i : 10]
    response = c.talk(str(l))






    print(f"Sending the {gene} Gene to the server...")
    response = c.talk(str(s))
    print(f"To server:{str(s)}")
    print(f"From server: {response}")
