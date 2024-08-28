# EX6.Create function to count positive number in array [-1,11,2,0,-1,4]

def sum(number):
    count_positive = 0
    for i in range(len(number)):
        if number[i] >= 0:
            count_positive += 1
        
    return count_positive
number_positive = [-1,11,2,0,-1,4]
print(sum(number_positive))