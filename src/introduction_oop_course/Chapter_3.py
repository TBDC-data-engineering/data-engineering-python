# Operator overloading: comparing objects
class BankAccount:
    # Modify to initialize a number attribute
    def __init__(self, number, balance=0):
        self.balance = balance
        self.number = number

    def withdraw(self, amount):
        self.balance -= amount

        # Define __eq__ that returns True if the number attributes are equal

    def __eq__(self, other):
        return self.number == other.number


# modify the equal to check the type
class BankAccount2:
    def __init__(self, number, balance=0):
        self.number, self.balance = number, balance

    def withdraw(self, amount):
        self.balance -= amount

        # Modify to add a check for the class type

    def __eq__(self, other):
        return (self.number == other.number) and (type(self) == type(other))


class Employee3:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary

    # Add the __repr__() method
    def __repr__(self):
        emp_str = f"Employee('{self.name}', {self.salary})"
        return emp_str

        # Add the __str__() method
    def __str__(self):
        emp_str = f"""Employee name: {self.name} Employee salary: {self.salary}"""
        return emp_str

# Exceptions
class SalaryError(ValueError):
    pass


class BonusError(SalaryError):
    pass


class Employee:
    MIN_SALARY = 30000
    MAX_BONUS = 5000

    def __init__(self, name, salary=30000):
        self.name = name
        if salary < Employee.MIN_SALARY:
            raise SalaryError("Salary is too low!")
        self.salary = salary

    # Raise exceptions
    def give_bonus(self, amount):
        if amount > Employee.MAX_BONUS:
            raise BonusError("The bonus amount is too high!")

        elif self.salary + amount < Employee.MIN_SALARY:
            raise SalaryError("The salary after bonus is too low!")

        self.salary += amount


if __name__ == '__main__':
    acct1 = BankAccount(123, 1000)
    acct2 = BankAccount(123, 1000)
    acct3 = BankAccount(456, 1000)
    print(acct1 == acct2)
    print(acct1 == acct3)

    emp1 = Employee3("Amar Howard", 30000)
    print(repr(emp1))
    emp2 = Employee3("Carolyn Ramirez", 35000)
    print(repr(emp2))
    print(emp2)


