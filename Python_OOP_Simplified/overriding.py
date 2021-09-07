class Employee:
    
    def setNumberOfWorkingHours(self):
        self.workingHorkingHours = 40
        
    
    def displayWorkingHours(self):
        print(self.workingHorkingHours)
        

class Trainee(Employee):

# To override the base class method
    def setNumberOfWorkingHours(self):
        self.workingHorkingHours = 45

# To use the base class method
    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours();
        

employee = Employee()
employee.setNumberOfWorkingHours()
print("The number of working hours of an employee is", end = ' ')
employee.displayWorkingHours()


trainee = Trainee()
trainee.setNumberOfWorkingHours()
print("The number of working hours of a trainee  is", end = ' ')
trainee.displayWorkingHours()


trainee.resetNumberOfWorkingHours()
print("The number of working hours of a trainee after reset is", end = ' ')
trainee.displayWorkingHours()
