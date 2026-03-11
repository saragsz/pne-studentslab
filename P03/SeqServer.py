import socket
from termcolor import colored
from Seq1 import Seq


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT = 8080
IP = "127.0.0.1"

ls.bind((IP, PORT))

ls.listen()

print("SEQ Server configured!")

while True:
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")

        ls.close()

        exit()

    else:
        print("A client has connected to the server!")

        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()

        cmd = msg.strip( ).split(" ",1)
        command = cmd[0]

        seq_list = ["ACGT","TGCT","CCGA","GTAC"]

        if command == "PING":

            color_msg = colored(cmd[0] + " " + "command" , "green")
            response = "OK!"

            print(f"{color_msg}")
            print("OK!")

        elif command == "GET":

            number = int(cmd[1])
            response = seq_list[number]
            print(seq_list[number])

        elif command == "INFO":
            seq = Seq(cmd[1])
            n_bases = seq.count()
            long = len(cmd[1])
            response = f"Sequence: {cmd[1]} \n Total lenght: {long}"

            for key, value in n_bases.items():
                percentage = (value / long) * 100
                perc_round = round(percentage,2)
                response += f" {key} : {value} ({perc_round} %)"

        elif command == "COMP":
            seq = Seq(cmd[1])
            response = seq.complement()

        elif command == "REV":
            seq = Seq(cmd[1])
            response = seq.reverse()

        elif command == "GENE":
            gene_name = cmd[1]
            file = f"../S04/sequences/{gene_name}.txt"
            seq = Seq()
            seq.read_fasta(file)
            response = str(seq)

        color_msg = colored(cmd[0] , "green")
        print(f"{color_msg}")

        cs.send(response.encode())
        cs.close()
        print(response)




