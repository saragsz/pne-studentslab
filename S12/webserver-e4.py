import socket
import termcolor

# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT:")

    # -- Split the request messages into lines
    lines = req.split('\n')

    # -- The request line is the first
    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    # --- READ HTML FILE ---
    with open("index.html", "r") as f:
        body = f.read()

    # -- Status line
    status_line = "HTTP/1.1 200 OK\n"

    # -- Headers
    header = "Content-Type: text/html\n"
    header += f"Content-Length: {len(body)}\n"

    # -- Build response
    response_msg = status_line + header + "\n" + body

    # -- Send response
    s.send(response_msg.encode())


# -------------- MAIN PROGRAM
# ------ Configure the server

# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Avoid "Address already in use"
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Bind IP and PORT
ls.bind((IP, PORT))

# -- Listen for connections
ls.listen()

print("Green server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped!")
        ls.close()
        exit()
    else:
        # -- Handle client
        process_client(cs)

        # -- Close connection
        cs.close()