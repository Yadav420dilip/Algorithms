"""
The knapsack problem is a problem in combinatorial optimization: Given a set of items,
each with a weight and a value, determine the number of each item to include in a collection
so that the total weight is less than or equal to a given limit and the total value is as large as possible.

Input data format:
items=[ ["Item name1", 'Item price1", "Item weight1"],
        ["Item name2", 'Item price2", "Item weight2"],]
"""

items = [
    ["item1", 10, 2],
    ["item2", 5, 3],
    ["item3", 15, 5],
    ["item4", 7, 7],
    ["item5", 6, 1],
    ["item6", 18, 4],
    ["item8", 3, 1]
]
knapsack_weight = 15
result = []
total_sum = 0

for item in items:  # for calculating the price/wieght
    item.append(round(item[1] / item[2], 2))

# After calculating the price/wieght data format is
"""
items=[ ["Item name1", 'Item price1", "Item weight1", "price per weight ratio 1 "],
        ["Item name2", 'Item price2", "Item weight2" ,"price per weight ratio 2 "],]
"""

items.sort(key=lambda x: x[3], reverse=True)  # Sorting the items in descending order on the basis of price per
# weight ratio

for greatest_item in items:
    if knapsack_weight - greatest_item[2] >= 0:
        knapsack_weight -= greatest_item[2]
        result.append(greatest_item)
    else:  # this part for calcuting the fraction of the item
        if knapsack_weight != 0:
            fraction_price = knapsack_weight * greatest_item[3]
            greatest_item[2] = knapsack_weight
            greatest_item[1] = fraction_price
            knapsack_weight -= knapsack_weight
            result.append(greatest_item)

for result_item in result:
    total_sum += result_item[1]

print("Item fit in the bag", result)
print("Maximum Price", total_sum)
