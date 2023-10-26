"""Practice with Dictionaries."""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
ice_cream["mint"] = 3
ice_cream.pop("mint")
print(ice_cream)

# Accessing a value
print(f"There are {ice_cream['chocolate']} orders of chocolate")

# Adjusting a value
ice_cream["vanilla"] = 10
print("After adjusting amount vanilla:")
print(ice_cream)

# Getting the length
print(f"The number of key value pairs: {len(ice_cream)}")

# Checking if a value is in a dictionary
print("Is chocolate in ice_cream?")
print("chocolate" in ice_cream)

# Using it in a conditional
if "mint" in ice_cream:
    print(f"Number of orders: {ice_cream['mint']}")
else:
    print("No orders of mint")

# Loop through and print out every flavor and its number of orders
for key in ice_cream:
    # print "<flavor>" has <num_orders> orders"
    print(f"{key} has {ice_cream[key]} orders.")