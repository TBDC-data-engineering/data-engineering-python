
class Employee:
    """This class is for the Employee"""
    __name = None
    __salary = None

    def __init__(self, name, salary=0):
        self.__name = name
        self.__salary = salary

    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        self.__salary = salary

    def give_salary_raise(self, amount:float):
        self.__salary += amount

    def identify(self):
        print(f"I am the employee {self.__name} my salary is {self.__salary}")



if __name__ == '__main__':
    ratio = 12 / 8
    print(dir(ratio))
    e2 = Employee(name="Silvio", salary=200)
    e = Employee("Silvio", 900)
    e.set_salary(100)
    e.set_name("John")
    e.identify()
    e.give_salary_raise(200)
    e.identify()

