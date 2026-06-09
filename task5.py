products = {
    "Rose": 100,
    "Lily": 150,
    "Tulip": 200
}

print("Products and Prices:")

for product, price in products.items():
    print(product, "=", price)

total = sum(products.values())

expensive_product = max(products, key=products.get)

print("\nTotal Price:", total)
print("Most Expensive Product:", expensive_product)
print("Price:", products[expensive_product])