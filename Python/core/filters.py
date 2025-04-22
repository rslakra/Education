# Author: Rohtash Lakra

class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    # string representation of this object
    def __str__(self) -> str:
        return f"Student <name={self.name}, score={self.score}>"
    
    # string representation of this object
    def __repr__(self) -> str:
        return f"{self.name}:{self.score}"

students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.75), Student("Jane", 0.84), Student("Sarah", 0.63), Student("Mary", 0.55)]
# print(students)

passed_list = list(filter(lambda student: student.score >= 0.7, students))
print(passed_list)

failed_list = list(filter(lambda student: student.score < 0.7, students))
print(failed_list)


numbers = [1, 2, 3, 4, 5]
result = list(filter(lambda num: num % 2 == 0, numbers))
print(result)

