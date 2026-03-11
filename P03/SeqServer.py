import socket
from termcolor import colored
from P01.Seq1 import Seq


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

        if cmd[0] == "PING":

            color_msg = colored(cmd[0] + " " + "command" , "green")
            response = "OK!"

            print(f"{color_msg}")
            print("OK!")

            cs.send(response.encode())
            cs.close()

        elif cmd[0] == "GET":
            number = int(cmd[1])

            color_msg = colored(cmd[0] + " " + "command", "green")
            response = seq_list[number]

            print(f"{color_msg}")
            print(seq_list[number])

            cs.send(response.encode())
            cs.close()

        elif cmd[0] == "INFO":
            seq = Seq(cmd[1])
            n_bases = seq.count()

            for key, value in n_bases.items():
                percentage = (value / len(cmd[1])) * 100
                perc_round = round(percentage,2)
                print (f"{key} : {value} ({perc_round})")






