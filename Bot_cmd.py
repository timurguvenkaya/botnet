import threading
import time


class BotCmd(threading.Thread):
    def __init__(self, qv2, socketthread):
        threading.Thread.__init__(self)
        self.q = qv2
        self.socketthread = socketthread

    def run(self):
        while True:
            SendCmd = str(input("BotCmd> "))
            if (SendCmd == ""):
                pass
            elif (SendCmd == "exit"):
                for i in range(len(self.socketthread)):
                    time.sleep(0.1)
                    self.q.put(SendCmd)
                time.sleep(5)
                os._exit(0)
            else:
                print("[+] Sending Command: " + SendCmd +
                      " to " + str(len(self.socketthread)) + " bots")
                for i in range(len(self.socketthread)):
                    time.sleep(0.1)
                    self.q.put(SendCmd)
