from Chapter_1 import Employee

"""Global Variable visible for all instance"""

class EmployeeStatic:
    MIN_SALARY = 5000

    def __init__(self, name, salary):
        self.name = name
        if salary < EmployeeStatic.MIN_SALARY:
            self.salary = EmployeeStatic.MIN_SALARY
        else:
            self.salary = salary

    """Class methods"""
    @classmethod
    def identify(cls):
        """cls Refers to the class"""
        print(f"I am the employee my salary is ")

# class methods example
class Person:
    CURRENT_YEAR = 2025

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Add a class method decorator
    @classmethod
    # Define the from_birth_year method
    # Object factory
    def from_birth_year(cls, name, birth_year):
        # Create age
        age = Person.CURRENT_YEAR - birth_year
        # Return the name and age
        return cls(name, age)


class BetterDate:
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    # Define a class method from_str
    @classmethod
    def from_str(cls, datestr):
        # Split the string at "-"
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        # Return the class instance
        return cls(year, month, day)

# Class inheritance

class Employee2:
    MIN_SALARY = 30000

    def __init__(self, name, salary=MIN_SALARY):
        self.name = name
        if salary >= Employee2.MIN_SALARY:
            self.salary = salary
        else:
            self.salary = Employee2.MIN_SALARY

    def give_raise(self, amount):
        self.salary += amount


# Define a new class Manager inheriting from Employee
class Manager(Employee2):
    # Add a keyword to leave this class empty
    pass


class Employee3:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount


class Manager3(Employee3):
    # Add a constructor
    def __init__(self, name, salary=50000, project=None):
        # Call the parent's constructor
        Employee3.__init__(self, name, salary)

        # Assign project attribute
        self.project = project

    def display(self):
        print("Manager ", self.name)

        # Add a give_raise method

    def give_raise(self, amount, bonus=1.05):
        new_amount = amount * bonus
        Employee3.give_raise(self, new_amount)


if __name__ == '__main__':

    e = Employee("Silvio", 900)
    e.identify()
    EmployeeStatic.identify()
    bob = Person.from_birth_year("John", 1990)
    print(bob)

    xmas = BetterDate.from_str("2024-12-25")
    print(xmas.year)
    print(xmas.month)
    print(xmas.day)

    #Inheritance
    # Define a Manager object
    mng = Manager("Debbie Lashko", 86500)

    # Print mng's name
    print(mng.name)
