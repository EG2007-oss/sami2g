def even():
    num = int(input("Enter a number: "))
    if num % 2 == 0 and num>0: # if true, it will print even no
        print("even no")
    elif num % 2 != 0 and num>0: # if true, it will print odd no
        print("odd no")
    if num > 0:
        print("positive no")
    elif num < 0:
        print("negative no")
    else:
        print("zero")
even()

def square_area(side):
    return side*side

def main():
    area = square_area(67)
    print(area)
    
main()