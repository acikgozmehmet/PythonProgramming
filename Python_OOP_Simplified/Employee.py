class Employee:
    # name = "Ben"
    # designation="Sales Executive"
    # salesMadeThisWeek=6
    # numberOfWorkingHours = 40
    
    # def hasAcvhievedTarget(self):
    #     if self.salesMadeThisWeek  >= 5:
    #         print("Target has been achieved")
    #     else:
    #         print("Target has NOT been achieved")

    def __init__(self, name):    
        self.__name = name
    
    # def employeeDetails(self):
    #     self.name = "Mehmet"
    #     print("Name = ", self.name)
    #     print("Class level Name = ",Employee.name)
    
    
    @staticmethod
    def welcomeMessage():
        print("Welcome to our organization")
        
        
    # def enterEmployeeDetails(self):
    #     self.name ="Mark"
        
    def displayEmployeeDetails(self):
        print(self.__name)
    
        
        
    
employeeOne = Employee("Mehmet")  
employeeTwo = Employee("Mark")  

employeeOne.displayEmployeeDetails()
employeeTwo.displayEmployeeDetails()

# employee.employeeDetails()
# Employee.employeeDetails(employee)
# employee.welcomeMessage()    
