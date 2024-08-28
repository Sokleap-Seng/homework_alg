# EX7.Create function to count negative number in array [-1,11,2,0,-1,4]

def sum(number):
    count_negative = 0
    for i in range(len(number)):
        if number[i] < 0 :
            count_negative += 1

    return count_negative
number_negative = [-1,11,2,0,-1,4,]
print(sum(number_negative))