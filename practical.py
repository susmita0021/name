num1=int(input("Enter first number: "))

num2=int(input("Enter second number: "))

num3=int(input("Enter Third number: "))

def highest():

    if(num1>=num2) and (num1>=num3):

        l=num

    elif(num2>=num1) and (num2>=num3):

         l=num2

    else:

         l=num3

    print("Largest number among  the three is",l)

highest()
