def input_information(user_input):
    """
    ask user to input a number and display information about it:
    even or odd
    positive or negative
    square of the number
    """
    user_input= int(input("Enter a number: "))
    if user_input % 2 == 0 and user_input>0: # if true, it will print even no
        print("even number")
    elif user_input % 2 != 0 and user_input>0: # if true, it will print odd no
        print("odd number")
    if user_input > 0: # if true, it will print positive number
        print("positive number")
    elif user_input < 0: # if true, it will print negative number
        print("negative number")
    else: # if both conditions are false, it will print zero
        print("zero")


def main():
    """
    ask user to input a number and display the square and cub of the number
    """
user_input = int(input("Enter a number: "))
print ('square of the number is',user_input**2) # this will print the square of the number
print(" the cub of the number is",user_input**3) # this will print the cub of the number
input_information(user_input) # call the function
main()