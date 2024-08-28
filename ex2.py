# EX2.Create function to sum odd number in array [1,2,3,4,5,6]

def sum(numbers):
    sum = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 1:
            sum += numbers[i]
    
    return sum
odd_number = [1,2,3,4,5,6]
print(sum(odd_number))