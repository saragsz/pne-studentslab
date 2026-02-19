from pathlib import Path
from process_exons import get_exons

def find_exons(filename,max_coord):
    exons = get_exons(filename)
    current_pos = 0
    n = 1
    print("Exon     Long.     Start    End")
          
    for seq in exons:
        lenght = len(seq)

        final = max_coord - current_pos
        inicio = final - lenght + 1
        print(f"{n} | {lenght} | {inicio} |{final}")

        current_pos += lenght
        n += 1

if __name__ == "__main__":
    find_exons("sequences/ADA.txt",44652852)



