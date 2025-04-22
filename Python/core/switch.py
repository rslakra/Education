#
# Author: Rohtash Lakra
#

import random

# Rider Class
class Rider:

    # __init__
    def __init__(self, name):
        self.name = name;
        self.age = random.randint(1, 100)
        self.direction = random.randint(1, 4)

    # check_eligibility
    def check_direction(self):
        match self.direction:
            case 1:                
                return "Left"
            case 2:
                return "Up"
            case 3:                
                return "Right"
            case 4:
                return "Down"
            case _:
                return "Invalid Direction"


    # ride
    def ride(self):
        self.message = ""
        if self.age < 5:
            self.message = "You can't ride any ride"
        elif self.age > 5 and self.age < 12:
            self.message = "You can ride only level 1 rides"
        elif self.age > 12 and self.age < 65:
            self.message =  "You can ride all levels"
        else:
            self.message = "You can ride upto level 2"

        print(f"\n{self.name}: {self.message}")


boy = Rider("Ryan")
boy.ride()
print(boy.check_direction())
# 
girl = Rider("Sarah")
girl.ride()
print(girl.check_direction())



def get_day_type(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "Weekday"
        case "Saturday" | "Sunday":
            return "Weekend"
        case _:
            return "Invalid day"


print(get_day_type("Monday"))
print(get_day_type("Saturday"))
print(get_day_type("Invalid"))
