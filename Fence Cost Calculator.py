# To calculate the cost of fencing for a rectangular area 
# Author Theophilia Tay
# Date: 28/05/2025
# Version 1

def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:
        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)
keep_going = ""
while keep_going =="":

    for item in range(0,1):
        width = num_check("What is the width of your fence?: ")
    print(width)

    print()

    for item in range(0,1):
        length = num_check("What is the length of your fence?: ")
    print(length)

    cost = int(input("What is the cost?: $"))

    perimeter = 2* (width+length)

    fencing_cost = (perimeter*cost)

    print()
    print(f"The perimeter is: {perimeter} units")
    print(f"The total cost is ${fencing_cost}")

    keep_going = input("Press <enter> to keep going or any other key to quit. ")
    print()
print("Thank you for using the Fencing Calculator!")