class Library:
    
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
        
        
    def displayAvailableBooks(self):
        print()
        print("Available Books")
        for i in range(len(self.availableBooks)):
            print(self.availableBooks[i])
            
            
    
    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            self.availableBooks.remove(requestedBook)
            print("You have the book")
        else:
            print("sorry, the book is not available in our list")
            
            
    
    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("You have returned the book")
    
    
class Customer:
    def requestBook(self):
        print("Enter the name of the book you would like to borrow : ")
        self.book = input()
        return self.book
        
    
    def returnBook(self):
        print("Enter the name of the book you would like to return : ")
        self.book = input()
        return self.book


library = Library(['A','B','C'])
customer = Customer()
# book = customer.requestBook()
# print(book)

while True:
    print("")
    print("1. Display books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")
    print("Enter your choice: ")
    choice = int(input())
    if choice is 1:
        library.displayAvailableBooks()
    elif choice is 2:
        book = customer.requestBook()
        library.lendBook(book)
    elif choice is 3:
        book = customer.returnBook()
        library.addBook(book)
    elif choice is 4:
        quit()
    else:
        print("Enter the correct choice")