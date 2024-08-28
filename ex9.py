# EX9.Create function to find average of price

# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]

def averge(products):
    average = 0
    for i in range(len(products)):
        average += products[i]["price"]/2
    
    return average
number_product = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
print(averge(number_product))                              