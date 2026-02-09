class Salary:
    def __init__(self,basic,allowance):
        self.basic = basic
        self.allowance = allowance

    def calculate_net_salary(self):
        net_salary = self.basic + self.allowance 
        return  net_salary
      
def __str__(self):
    return "basic : "+ str(self.basic) + " allowance : "+ str(self.allowance) + "net salary"+ str(self.calculate_net_salary())