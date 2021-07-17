import socket


class Alarm:
    def __init__(self, sever_name, sever_port):
        self.g_open = b"\xA0\x01\x00\xA1"
        self.g_close = b"\xA0\x01\x01\xA2"

        self.y_open = b"\xA0\x02\x01\xA3"
        self.y_close = b"\xA0\x02\x00\xA2"

        self.r_open = b"\xA0\x03\x01\xA4"
        self.r_close = b"\xA0\x03\x00\xA3"

        self.s = self.connect(sever_name, sever_port)

    def connect(self, sever_name, sever_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((sever_name, sever_port))
        return s

    def close(self):
        self.s.close()

    def set_green(self):
        # self.s.send(self.r_close)
        # self.s.send(self.y_close)
        self.s.send(self.g_open)

    def set_yellow(self):
        self.s.send(self.g_close)
        self.s.send(self.r_close)
        self.s.send(self.y_open)

    def set_red(self):
        self.s.send(self.g_close)
        # self.s.send(self.y_close)
        # self.s.send(self.r_open)
