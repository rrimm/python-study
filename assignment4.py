# 1. Write a Car class that has the following properties: registration number, maximum speed, current speed and travelled distance. Add a class initializer that sets the first two of the properties based on parameter values. The current speed and travelled distance of a new car must be automatically set to zero. Write a main program where you create a new car (registration number ABC-123, maximum speed 142 km/h). Finally, print out all the properties of the new car.
class Car:
    def __init__(self, registration_number, maximum_speed, current_speed = 0, travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

new_car = Car('ABC-123', 142)

print(new_car.registration_number)
print(new_car.maximum_speed)
print(new_car.current_speed)
print(new_car.travelled_distance)

# 2. Extend the program by adding an accelerate method into the new class. The method should receive the change of speed (km/h) as a parameter. If the change is negative, the car reduces speed. The method must change the value of the speed property of the object. The speed of the car must stay below the set maximum and cannot be less than zero. Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h. Then print out the current speed of the car. Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed. The travelled distance does not have to be updated yet.
class Car:
    def __init__(self, registration_number, maximum_speed, current_speed, travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        if self.current_speed < 0:
            self.current_speed = 0

        return self.current_speed

new_car = Car('ABC-123', 250, 90)

new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)
new_car.accelerate(-200)

print(f'The final speed: {new_car.current_speed}')