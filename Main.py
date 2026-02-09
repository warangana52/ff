import Salary
from Employee import Employee


def display_menu():
    print("***************************")
    print("*****welcome*****")
    print("Main Menu")
    print("1. create employee")
    print("2. create salary")
    print("3. exit")
    print("***************************")
    
    while True:
        option = input("enter your option")
        if (option.isdigit() and option in ["1","2","3"]):
            option = int(option)
            break
        else:
            print("valid input")    
    return option

def employee():
    name =input( "enter your name" )       
    ID = input ("enter your id")
    department =input ("enter your department"  )
    designation = input("enter your designation")
    emp = Employee(name,ID,department,designation)
    print(emp)


def salary():
     while True : 
            basic = input("Enter Basic Salary: ")
            if basic.replace(".","").isdigit():
                basic =float(basic)
                break
            else:
                print("enter valid basic salary")

            while True :    
                allowance = input("Enter Allowance: ")   
                if allowance.replace(".","").isdigit():
                    allowance =float(allowance)
                    break
                else:
                    print("enter valid basic allowance")

                sal = Salary.Salary(basic, allowance)  
                print(sal.calculate_net_salary()) 
                sal_1 = Salary.Salary(3000, 500)
                print(sal_1.calculate_net_salary())    



def main():
    option = display_menu()
    if option == 1:
        employee()
            
    elif option == 2:
        salary()   
       
    else:
        exit()
   


if __name__== "__main__":
    main()    