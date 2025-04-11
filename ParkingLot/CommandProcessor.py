from Command import Command
from ParkingLot import ParkingLot
from Car import Car
# The initial function which is called, which is responsible for executing commands
# Input: List of Commands
# Output: Command Ouputs

parking_lot = None

def process(command_list: list[str]) -> list[str]:

    # Interact with each element of the parking lot structure
    # - Car.py
    # - ParkingLot.py
    # - Ticket.py

    global parking_lot

    output_list = []

    for current_command in command_list:
        if current_command.command == "create_parking_lot":
            parking_lot = ParkingLot(int(current_command.args[0]))
            output_list.append("Created Parking Lot with Capacity " + current_command.args[0])
        
        elif current_command.command == "park":
            new_car = Car(current_command.args[0], current_command.args[1])
            output_list.append(parking_lot.add_car(new_car))

        elif current_command.command == "status":
            output_list.append(parking_lot.status())
        
        elif current_command.command == "leave":
            slot_number = int(current_command.args[0])
            output_list.append(parking_lot.remove_car(slot_number))

        elif current_command.command == "registration_numbers_for_cars_with_colour":
            color = current_command.args[0]
            output_list.append(parking_lot.color_to_reg(color))

        elif current_command.command == "slot_numbers_for_cars_with_colour":
            color = current_command.args[0]
            output_list.append(parking_lot.color_to_slot(color))

        elif current_command.command == "slot_number_for_registration_number":
            reg = current_command.args[0]
            output_list.append(parking_lot.registration_to_slot(reg))
        
        else:
            raise("Unkown command!")

    return output_list