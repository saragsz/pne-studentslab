seq = input("Please introduce a DNA sequence:")
count = 0
A = 0
C = 0
G = 0
T = 0
for b in seq:
    count += 1
    if b == "A":
        A += 1
    elif b == "C":
        C += 1
    elif b == "G":
        G += 1
    elif b == "T":
        T += 1


print("Total lenght:", count)
print("A:", A)
print("C:", C)
print("G:", G)
print("T:", T)



