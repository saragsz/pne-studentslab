dna = "ATGCGATCGATCGATCGATCGA"

print("Lenght:",len(dna),"letters")
print("First 5:",dna[0:5])
print("Last 3:",dna[-3:])
print("Lower case:",dna.lower())
print("ATC count:", dna.count("ATC"))
print("RNA:",dna.replace("T","U"))