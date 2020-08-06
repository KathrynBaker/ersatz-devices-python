"""
This will watch the com port
"""

import load_setup
import socket


class Instrument:
    def __init__(self, port, name):
        self.port = port
        self.name = name
        self.commands = load_setup.load_setup(name)
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ss.bind((socket.gethostname(), port))
        self.ss.listen(5)

    def run(self):
        print("Run is running")
        while True:
            # Need to add the code to listen to the COM port in here
            cs, add = self.ss.accept()
            cmd = cs.recv(1024).decode()
            cmd = cmd.strip()
            if cmd != "":
                print(cmd)
            if cmd == "QUIT":
                break
            command = str(cmd).split(" ")
            if len(command) < 2:
                command.append("")
            result = self.commands.run_command(command[0].strip(), command[1].strip()) + "\r\n"
            cs.send(result.encode('ascii'))
            cs.close()
        print("Quitting")

    def cease(self):
        self.ss.close()


def start_ibex_example(port=9998, name="stacia"):
    example = Instrument(port, name)
    example.run()
    example.cease()


# Whilst trying to get running with tcp
start_ibex_example()
