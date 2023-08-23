class Vehicle:
    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number= wheel_number

    def go(self):
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        return "filling up!"

# v1 = Vehicle("large", 4)
# print(v1.wheel_size)  
# print(v1.wheel_number)        

