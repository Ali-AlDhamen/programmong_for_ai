
class Employee:
    def __init__(self, id,name):
        self.id = id
        self.name = name
    
    
    def print_info(self):
        print(self)
       
    @staticmethod 
    def welcome_fun():
        print(f"Welcome to AI company")
        
    def __str__(self):
        return f"Id: {self.id}\nName: {self.name}"
    
    def __del__(self):
        print("Employee deleted")
        
        


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary
        
    
    def calculate_payroll(self):
        return self.weekly_salary
        
    def __str__(self):
        return super().__str__() + f"\nweekly salary: {self.weekly_salary}"
    
    def __del__(self):
        print("SalaryEmployee deleted")
        


class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate
        
    
    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate
        
    def __str__(self):
        return super().__str__() + f"\nhours worked: {self.hours_worked}\nhour rate: {self.hour_rate}"
    
    def __del__(self):
        print("HourlyEmployee deleted")
        
        


Employee.welcome_fun()
s_emp = SalaryEmployee(1, "Ahmed", 1000)
h_emp = HourlyEmployee(2, "Ali", 40, 10)

print(s_emp)
print(f'Payroll: {s_emp.calculate_payroll()}')
print(h_emp)
print(f'Payroll: {h_emp.calculate_payroll()}')



