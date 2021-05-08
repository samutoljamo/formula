import socket, time
HOST = ''
PORT = 2000
def default(*args, **kwargs):
    pass
class Server:
    def __init__(self, on_connect=default, on_disconnect=default, handle_msg=default, msg_len=1):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.on_connect = on_connect
        self.on_disconnect = on_disconnect
        self.handle_msg = handle_msg
        self.msg_len = msg_len
        self.buf = b""

    def run(self):
        self.socket.bind((HOST, PORT))
        self.socket.listen(1)
        while True:
            conn, addr = self.socket.accept() # no threading, accept one client at a time
            self.on_connect(addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    self.buf = b""
                    break
                self.buf += data
                self.consume_buffer()
            self.on_disconnect()
            conn.close()
    def consume_buffer(self):
        print(self.buf)
        for byte in self.buf:
            self.handle_msg(byte)
        self.buf = b""

if __name__ == '__main__':
    def handle(msg):
        print(msg)
    s = Server(handle_msg=handle)
    s.run()

