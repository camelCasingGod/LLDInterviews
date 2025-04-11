from Command import Command

def parse(commands: str) -> list:    
    list_of_commands = []

    for command in commands.split("\n"):
        command_elements = command.split(" ")
        curr_command = Command(command_elements[0], command_elements[1:])

        list_of_commands.append(curr_command)

    return list_of_commands