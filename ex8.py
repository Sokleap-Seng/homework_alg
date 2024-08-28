# EX8.Create function to sum total of price 
# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]

def sum(products):
    total = 0
    for i in range(len(products)):
        if products[i]["price"]:
            total += products[i]["price"]

    return total
total_products =  [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
print(sum(total_products))
    