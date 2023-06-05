class Worker:
    def __init__(self, name, surname, rate, days):
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_rate(self):
        return self.__rate

    def get_salary(self):
        return self.__rate * self.__days

    def get_bonus(self, bonus):
        return (self.__rate * self.__days * bonus) + self.__rate * self.__days

    def get_info(self):
        return f"Name: {self.__name}\nSurname: {self.__surname}\n" \
               f"Rate: {self.__rate}\nDays: {self.__days}\nSalary: {self.get_bonus(0.15)}\n"

Worker2 = Worker("Аруг", "Заруб",1500,28)
Worker1 = Worker("Капут","Найн",700,15)


print(Worker.get_info(Worker1))
print(Worker.get_info(Worker2))
print("Сумма",Worker1.get_bonus(0.15)+Worker2.get_bonus(0.15))
