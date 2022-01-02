def adder(*numbers):
    if len(numbers) > 5:
        print("Max 5 value allowed. Retry!")
        return None
    my_sum = 0
    for i in numbers:
        my_sum = my_sum + i
    return my_sum

print(adder(1,2,3,4,5))
print(adder(1,2))
print(adder(1,1,1,1,1,1,1,1))