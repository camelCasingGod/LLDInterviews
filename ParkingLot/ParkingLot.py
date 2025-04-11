import heapq
from collections import defaultdict
import Car

class ParkingLot:

    def __init__(self, number_of_cars: int):
        self.max_cars = number_of_cars
        self.parking_slots = [None for _ in range(self.max_cars)]
        self.vacancies = [slot + 1 for slot in range(self.max_cars)]
        heapq.heapify(self.vacancies)
        self.car_to_slot = {}
        self.color_to_slots = defaultdict(set)
        self.reg_to_slot = {}

    def add_car(self, car):
        # find an empty parking slot
        # update vacancies
        # update parking_slots
        # update reg_to_slot
        # update color_to_slots

        if len(self.reg_to_slot) == self.max_cars:
            return "Sorry parking lot is full"
        
        min_slot = heapq.heappop(self.vacancies) - 1
        self.parking_slots[min_slot] = car
        self.reg_to_slot[car.reg] = min_slot
        self.color_to_slots[car.color].add(min_slot)

        return "Allocated Slot Number: " + str(min_slot + 1)
    
    def remove_car(self, slot_number):
        # make sure that slot is occupied
        # update vacancies
        # update parking_slots
        # update reg_to_slot
        # update color_to_slots

        internal_slot = slot_number - 1
        if not self.parking_slots[internal_slot]:
            return "Car Doesn't Exist in Slot " + str(slot_number)
        
        leaving_car = self.parking_slots[internal_slot]
        heapq.heappush(self.vacancies, slot_number)
        self.parking_slots[internal_slot] = None
        del self.reg_to_slot[leaving_car.reg]
        self.color_to_slots[leaving_car.color].remove(internal_slot)
        return "Slot number " + str(slot_number) + " is free"

    def status(self):
        output_list = []
        output_list.append("Slot No. Registration No Colour")
        
        for slot in range(self.max_cars):
            current_car = self.parking_slots[slot]
            if current_car:
                output_list.append(str(slot + 1) + " " + current_car.reg + " " + current_car.color)
            # else:
            #     output_list.append(str(slot + 1) + " EMPTY")

        return "\n".join(output_list)

    def color_to_reg(self, color):
        # color -> slots
        # slots -> cars
        # cars -> reg
        reg_list = []
        for slot in self.color_to_slots[color]:
            current_car = self.parking_slots[slot]
            reg_list.append(current_car.reg)
        
        return ", ".join(reg_list)
    
    def color_to_slot(self, color):
        
        slot_list = []
        for slot in self.color_to_slots[color]:
            slot_list.append(str(slot + 1))
        
        return ", ".join(slot_list)

    def registration_to_slot(self, reg):
        
        return self.reg_to_slot[reg] if reg in self.reg_to_slot else "Not Found"
    