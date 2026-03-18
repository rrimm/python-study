# 1. Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters. The elevator has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor. If you make elevator h for example the method call h.go_to_floor(5), the method calls either the floor_up or floor_down methods as many times as it needs to get to the fifth floor. The methods run the elevator one floor up or down and tell what floor the elevator is after each move. Test the class by creating an elevator in the main program, tell it to move to a floor of your choice and then back to the bottom floor.
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.floor = bottom_floor

    def go_to_floor(self, floor):
        while True:
            if floor < self.floor:
                self.floor_down()

            elif floor > self.floor:
                self.floor_up()

            else:
                break

        return self.floor

    def floor_up(self):
        self.floor += 1
        print(f'The floor is now {self.floor}')

    def floor_down(self):
        self.floor -= 1
        print(f'The floor is now {self.floor}')

h = Elevator(1, 15)
h.go_to_floor(5)
h.go_to_floor(2)
h.go_to_floor(8)

# bottom floor
h.go_to_floor(1)

# 2. Extend the previous program by creating a Building class. The initializer parameters for the class are the numbers of the bottom and top floors and the number of elevators in the building. When a building is created, the building creates the required number of elevators. The list of elevators is stored as a property of the building. Write a method called run_elevator that accepts the number of the elevator and the destination floor as its parameters. In the main program, write the statements for creating a new building and running the elevators of the building.
class Elevator:
    def __init__(self, bottom_floor, top_floor, identifier):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.floor = bottom_floor
        self.identifier = identifier

    def go_to_floor(self, floor):
        while True:
            if floor < self.floor:
                self.floor_down()

            elif floor > self.floor:
                self.floor_up()

            else:
                break

        return self.floor

    def floor_up(self):
        self.floor += 1
        print(f'[elevator {self.identifier}] The floor is now {self.floor}')

    def floor_down(self):
        self.floor -= 1
        print(f'[elevator {self.identifier}] The floor is now {self.floor}')

class Building:
    def __init__(self, bottom_floor, top_floor, elevator_count):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevator_count = elevator_count
        self.elevators = [Elevator(bottom_floor, top_floor, index + 1) for index in range(elevator_count)]

    def run_elevator(self, elevator_id, destination_floor):
        if elevator_id == 0:
            raise Exception('The number of the elevator is not valid')

        if destination_floor > self.top_floor:
            raise Exception('The destination floor is higher than the top floor')

        # Although our course used list indexing, objects should be retrieved by their identifiers
        # elevator = next((elevator for elevator in self.elevators if elevator.identifier == elevator_id), None)
        elevator = self.elevators[elevator_id - 1]
        elevator.go_to_floor(destination_floor)

new_building = Building(1, 11, 4)

new_building.run_elevator(1, 6)
new_building.run_elevator(3, 10)
