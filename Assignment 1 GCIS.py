def input_information(user_input):
    """
    ask user to input a number and display information about it:
    even or odd
    positive or negative
    square of the number
    """
    num = int(input("Enter a number: "))
    if num % 2 == 0 and num>0: # if true, it will print even no
        print("even number")
    elif num % 2 != 0 and num>0: # if true, it will print odd no
        print("odd number")
    if num > 0: # if true, it will print positive number
        print("positive number")
    elif num < 0: # if true, it will print negative number
        print("negative number")
    else: # if both conditions are false, it will print zero
        print("zero")

def main():
    """
    ask user to input a number and display the square and cub of the number
    """
user_input = int(input("Enter the side of the square: "))
print ('square of the number is',user_input**2)
print(" the cub of the number is",user_input**3)
input_information(user_input)
main()