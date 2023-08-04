class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"employee name:{self.name} id:{self.id}")


class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def count_pay(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name, id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def count_pay(self):
        return self.daily_salary * self.work_days


emp1 = FullTimeEmployee("Zzk", "1001", 6000)
emp2 = PartTimeEmployee("Lhx", "1002", 230, 15)


