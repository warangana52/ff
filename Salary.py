class Salary:
    def __init__(self,basic,allowance):
        self.basic = basic
        self.allowance = allowance

    def calculate_net_salary(self):
        return self.basic + self.allowance    

basic = input("Enter Basic Salary: ")
if basic.replace(".","").isdigit():
    basic =float(basic)

    
allowance = input("Enter Allowance: ")   
if allowance.replace(".","").isdigit():
    allowance =float(allowance)

sal = Salary(basic, allowance)  
print(sal.basic) 
print(sal.calculate_net_salary()) 
sal_1 = Salary(3000, 500)  