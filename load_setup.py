"""
The contents of this file are all about loading in the setup information
"""

import commresp


def load_setup(filename):
    commands = commresp.CommResp()
    file = open(filename, 'r')
    contents = file.readlines()
    file.close()
    lines = list()
    for line in contents:
        lines.append(line.split(","))
    for line in lines:
        parameter = str(line[0]).strip()
        getter = str(line[1]).strip()
        setter = str(line[2]).strip()
        source = (str(line[3]).strip(), str(line[4]).strip(), str(line[5]).strip())
        commands.add_command(parameter, getter, setter, source)
    return commands
