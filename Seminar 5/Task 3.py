marks = int(input('ведите оценки:\n'))
achievement = []
while marks !=6:
    achievement.append(marks)
    marks = int(input())
number = len(achievement)
number5 = achievement.count(5)
print(number5/number * 100)