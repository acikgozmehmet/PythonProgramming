class OperatingSystem:
    multithreading = True
    name = "Mac OS"
    
    
class Apple:
    website = "www.apple.com"
    name = "Apple"
    
class MacBook(OperatingSystem, Apple):
    def __init__(self):
        if self.multithreading :
            print("Thus is a multitasking system. Visit {} for more information".format(self.website))
            print("Name :", self.name)
            
            
macBook = MacBook()
