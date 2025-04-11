import CommandParser
import CommandProcessor
import Logger

# The main function, in charge of facilitating the calling of all the other functions defined.
# Input: List of commands (From requirements)
# Output: Output log of commands (From requirements)

def Main() -> None:

    # List of String Commands -> List of Arguments to Function Calls
    # - CommandParser.py
    # Go through every function call, and execute it with appropriate function
    # - CommandProcessor.py
    # Store results in a List of Strings
    # - Keep a List in this class
    # Print every resulting log message in a list of strings
    # - Logger.py

    while True:
        command = input("$ ")
        if command == "exit":
            break
        command_list = CommandParser.parse(command)
        output_list = CommandProcessor.process(command_list)
        Logger.log(output_list)
    
Main()