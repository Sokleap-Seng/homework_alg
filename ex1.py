# EX1.Create function to sum numbers in array [1,2,3,4,5,6]

def sum(numbers):
    sum = 0
    for i in range(len(numbers)):
       sum += int(numbers[i])

    return sum
sum_number = [1,2,3,4,5,6]
print(sum(sum_number))