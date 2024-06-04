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

total = 0
for student in students:
    total += student.score

count = len(students)
print(total / count)


from functools import reduce

total_score = reduce(lambda total, student: total + student.score, students, 0)
print(round(total_score / len(students), 2))

print("\nFiltered with name start with 'M'")
# m_students = list(filter(lambda student: student.name.startswith('M'), students)) # starts with M
# m_students = list(filter(lambda student: student.name[0] == 'M', students)) # 1st char
# m_students = list(filter(lambda student: student.name[1] == 'a', students)) # 2nd char
m_students = list(filter(lambda student: student.name[-1] == 'h', students)) # last char
print(m_students)


print("\nReduce")
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda result, num: result * num, numbers)
print(result)

