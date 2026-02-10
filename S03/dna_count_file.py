#sequences = ["AGTACACTGGT","ACCAGTGTACT","ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"]
#print("From variable:",sequences)

#Option 1
f = open("dna.txt.","r")
lines = f.readlines()
f.close()

#Option 2
with open("dna.txt.","r") as f:
    lines = f.readlines()


total_number = 0
bases = {"A": 0, "C": 0, "T": 0, "G": 0}
for seq in lines:
    seq = seq.strip() #this function remove spaces and newline characters at the end of the string
    total_number += len(seq)
    for base in seq:
        if base in bases:
            bases[base] += 1

for base,count in bases.items():
    print(f'{base}:{count}')

print ("Total number of bases", total_number)







