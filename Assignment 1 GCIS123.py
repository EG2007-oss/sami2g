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

else: # if false, it will print odd number
        print("odd number")

if user_input > 0: # if true, it will print positive number
        print("positive number")
else: # if false, it will print negative number
        print("negative number")

print ('square of the number is',user_input**2) # this will print the square of the number
print(" the cub of the number is",user_input**3) # this will print the cub of the number

def main():
    user_input = int(input("Enter a number: ")) # asl the user to input a number
input_information(user_input) # call the function
main()