# Author: Rohtash Lakra

import random

# Rider Class
class Rider:

    # __init__
    def __init__(self, name):
        self.name = name;
        self.age = random.randint(1, 100)

    # check_eligibility
    def check_eligibility(self):
        if self.age < 5:
            return False
        elif self.age > 5 and self.age < 12:
            return False
        else:
            return True
        
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

# 
girl = Rider("Sarah")
girl.ride()