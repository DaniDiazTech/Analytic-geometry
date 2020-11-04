from analytic_functions import FindInTheLine

def main():
    while True:
        try:
            x1, y1 = input("Your first coordinate >> ").split(",")
            
            x2, y2 = input("Your second coordinate >> ").split(",")
            
            points = FindInTheLine(int(x1), int(y1), int(x2), int(y2)) 
            
            operation = input("What function do you want ? >> ")
            
            if operation == "d" or operation == "D":
            
                print(f"The distance between the points is {points.distance()}")
            
            elif operation == "m" or operation == "M":
            
                x_axis, y_axis  = points.midpoint() 
            
                print(f"The midpoint is: {x_axis} in X and {y_axis} in Y")
            
            elif operation == "s" or operation == "S":

                s, s_degrees = points.slope()                    
                print(f"The slope of the two coors is {s}, in degrees is {s_degrees} °")
            
            elif operation == "q" or operation == "quit" or x1 == "q" or y1 == "q" or x2 == "q" or y2 == "q":
                
                print("Thanks for use the program")
                break

        except ValueError as v:

            print(v)

            print("Error:Maybe you had type a string instead of a number, or just typed a number instead of two")

            pass


if __name__ == "__main__":
    print(
        """
        Created by Daniel Diaz

        This is a calculator that finds information of two coordinates
        Remember to type the correct values of x (first) and y (second) axis.

        Type the coordinates with a ',' between them. 

        Choose the function that you want:

        d(find distance between two coordinates)
        m(find the midpoint between two coordinates, returns the x and y axis)
        s(calculates the slope of two coordinates)
        q or quit (Quit the program)
        """
    )
    main()    
