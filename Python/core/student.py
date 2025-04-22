# Author: Rohtash Lakra

class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self) -> str:
        return f"Student <name={self.name}, score={self.score}>"

students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.75), Student("Jane", 0.84), Student("Sarah", 0.63), Student("Mary", 0.55)]

results = []
for student in students:
    # if student.score >= 0.7:
    #     results.append(f"{student.name} passed")
    # else:
    #     results.append(f"{student.name} failed")

    results.append(f"{student.name} passed") if student.score >= 0.7 else results.append(f"{student.name} failed")


map_results = list(map(lambda student: f"{student.name} passed" if student.score >= 0.7 else f"{student.name} failed", students))
print(map_results)


numbers = [1, 2, 3, 4, 5]

map_nums = list(map(lambda num : num * 2, numbers))
print(map_nums)

# print(results)
