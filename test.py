import os
import json
from pprint import pprint

directory_in_str = 'data'

directory = os.fsencode(directory_in_str)


list = os.listdir(directory_in_str) # dir is your directory path
number_files = len(list) # holds number of files in a certain directory


allProducts = {}
products= []

results = []
productInfo = []
qty = 0


for file in os.listdir(directory):
    filename = os.fsdecode(file)
    # print(filename)
    with open(f"data/{filename}") as f:
        results.append(json.load(f))


for x in results:
    for i in x['products']:
        productInfo.append(i)


for p in productInfo:
    if p['product_name'] == "Lychee Nuts":
        qty += p['qty_sold']
        allProducts["product_name"] = p['product_name']
        allProducts["qty_sold"] = qty


products.append(allProducts)


# if x['product_name'] not in productInfo:
# print(productInfo)
# print(number_files)
# print(f"Lychee Nuts QTY:{qty}")
# print(allProducts)
# print(productInfo)
print(products)