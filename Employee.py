from Status import Status
class Employee:
    def __init__(self,name, ID, department, designation):
        self.name = name
        self.ID = ID
        self.department = department
        self.designation = designation
        self.Status = Status.Active

name = "wara"        
ID = 1234
department = "it"  
designation = "ceo"
status = ""

emp = Employee(name,ID,department,designation,)
emp_1 = Employee("nimal",134,"hr","manager",)

