"""
The class for the setup info
"""

import generate_values


class CommResp:
    def __init__(self):
        self.command_list = list()
        self.get_command_list = list()
        self.set_command_list = list()
        self.command_dict = {}
        self.parameter_dict = {}
        self.static_dict = {}
        self.noresp_list = list()
        self.set_reset_dict = {}
        self.values = generate_values.GenerateValues()

    def add_command(self, parameter, getter, setter, source):
        if not getter == "na":
            self.command_list.append(getter)
            self.get_command_list.append(getter)
        if not setter == "na":
            self.command_list.append(setter)
            self.set_command_list.append(setter)
        self.command_dict[parameter] = source
        if source[0] == "static":
            self.static_dict[parameter] = source[1]
        elif source[0] == "na":
            self.noresp_list.append(parameter)
        elif source[0] == "var":
            if source[1] == "set_reset":
                self.set_reset_dict[parameter] = "Initial"
        self.parameter_dict.update({getter: parameter, setter: parameter})

    def get_source(self, command):
        parameter = self.get_parameter(command)
        if parameter is not None:
            return self.command_dict[parameter]
        else:
            return None

    def get_source_from_parameter(self, parameter):
        if parameter is not None:
            return self.command_dict[parameter]
        else:
            return None

    def get_parameter(self, command):
        if self.check_command(command):
            return self.parameter_dict[command]
        else:
            return None

    def check_command(self, command):
        valid = True
        if command not in self.command_list:
            valid = False
        return valid

    def run_command(self, command, value=None):
        if not self.check_command(command):
            return "Unknown Command"
        if command in self.get_command_list:
            return self.get_command_act(command)
        else:
            return self.set_command_act(command, value)

    def get_command_act(self, command):
        parameter = self.get_parameter(command)
        if parameter in self.static_dict.keys():
            return str(self.static_dict[parameter])
        if parameter in self.noresp_list:
            return "OK"
        source = self.get_source_from_parameter(parameter)
        if source is None:
            return "Error"
        else:
            if source[1] == "set_reset":
                return str(self.set_reset_dict[parameter])
            elif source[1] == "rand_dbl":
                return str(self.values.random_value("dbl"))
            else:
                return "Error"

    def set_command_act(self, command, value):
        parameter = self.get_parameter(command)
        if parameter in self.static_dict.keys():
            return "Unable to apply value"
        if parameter in self.noresp_list:
            return "OK"
        source = self.get_source_from_parameter(parameter)
        if source is None:
            return "Error"
        else:
            if value is None:
                return "No value given"
            if source[1] == "set_reset":
                self.set_reset_dict[parameter] = value
                return "Value set"
            elif source[1] == "rand_dbl":
                return "Value set"
            else:
                return "Error"

    def __str__(self):
        return str(self.command_list)
