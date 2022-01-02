starting = int(inputt("Enter the starting number"))
end = int(input("Enter the end range"))

while (starting <= end):
    if (starting % 7==0):
        print(starting,"is divisible by 7")
        starting += 1