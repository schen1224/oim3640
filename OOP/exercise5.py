class Employee(object):

    total_first_name = []
    sorted_list=[]
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + last + "@google.com"
        self.pay = pay
        if not self.first in Employee.total_first_name:
            Employee.total_first_name.append(first)
            Employee.sorted_list=sorted(Employee.total_first_name)

    def pay_aftertax(self):
        return self.pay * 0.9

    def __str__(self):
        return (
            self.first
            + " "
            + self.last
            + " "
            + self.email
            + " "
            + str(self.pay)
            + str(self.pay_aftertax)
        )


emp_1 = Employee("Sabrina", "Chen", 100000)
emp_2 = Employee("Daming", "Jiang", 50000)
emp_3 = Employee("Jason", "Jiang", 50000)
# print(Employee.pay_aftertax(emp_1))
print(Employee.total_first_name)
print(Employee.sorted_list)
