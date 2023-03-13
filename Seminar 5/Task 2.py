marks = int(input())
achievement = []
while marks !=6:
    achievement.append(marks)
    marks = int(input())
number = len(achievement)
number3 = achievement.count(3)
number4 = achievement.count(4)
number5 = achievement.count(5)
print((number3 + number4 + number5)/number * 100)