# Get input from the user
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

# Draw the rectangle
for i in range(width):  # width is number of rows
    print("*" * length)  # length is number of columns
