class Square():
    def __init__(self, side):
        self.side = side
        
    # Please note the special name of the operator -> "add : +"" 
    def __add__(square1, square2):
        return ( 4 * square1.side + 4 * square2.side )
    

squareOne = Square(5)
squareTwo = Square(10)
print("Sum of both sides of square = ", squareOne + squareTwo)