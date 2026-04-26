# ## Inventory Dictionary Program

# Item names with quantity and price are stored in an inventory dictionary:

# ```python
# inventory = {
#     "Laptop": (10, 45000),
#     "Mouse": (85, 350),
#     "Keyboard": (40, 750),
#     "Monitor": (6, 12000)
# }
# ```
# In the given tuples:
# * First value represents **quantity**
# * Second value represents **price per unit**

inventory = {
    "Laptop": (10, 45000),
    "Mouse": (85, 350),
    "Keyboard": (40, 750),
    "Monitor": (6, 12000)
}
print(type(inventory))


#------------------------------------------------------------------
# QQQQ a) Print all item names along with their quantity and price.

#print(inventory) --> directly prints dict

# for keys_ivt ,val_ivt in inventory.items(): #items --> = best way to iterate key + value together
#     print(keys_ivt,":",val_ivt)


print("\na) Print all item names along with their quantity and price.")

for item, (qty, price) in inventory.items():
    print("item name-", item,"=> Quantity: ",qty," Price: ", price)


#------------------------------------------------------------------
# b) Calculate and print the stock value of each item using:
# `stock_value = quantity × price`
# Also print the **total stock value** of all items.


print("\nb ) Calculate and print the stock value of each item using:")

stock_value=0
total_stock_value=0

for item,(quantity,price) in inventory.items():

    stock_value=quantity*price
    print("Items - ",item,": stock val -", stock_value)

    total_stock_value += stock_value

print("total stock value is : ",total_stock_value)


#------------------------------------------------------------------
# c) Accept an item name and new quantity from the user.

# * If the item exists, update its quantity.
# * Otherwise, print **"Item not found"**.



print("\nc) Accept an item name and new quantity from the user.")

add_item = input("Item name :").strip().title()
add_qnt = int(input("new quantity :").strip())

print(add_item)

for item,(quantity,price) in inventory.items():
    i=True
    if i == True:
        if add_item==item:
            print(add_item, "found in invetory")
            print("old price",inventory[add_item])
            inventory[add_item]=(add_qnt,price)

            print("new updated item qntyty is :", inventory[add_item])
            i=False;
    else:
        print(add_item,"Item not found")
        


#------------------------------------------------------------------
# d) Write a function `get_stock_status(quantity)` which accepts quantity as a parameter and returns:

# * If quantity is less than 8 → `"Critical Stock"`
# * If quantity is between 8 and 20 → `"Low Stock"`
# * If quantity is between 21 and 50 → `"Adequate Stock"`
# * If quantity is greater than 50 → `"High Stock"`

# Use this function to display the stock status for each item.

def get_stock_status(quantity):
    if quantity > 50:
        return "High Stock"
    elif quantity <= 50 and quantity >= 21:
        return "Adequate Stock"
    elif quantity <= 20 and quantity >= 8:
        return "Low Stock"
    elif quantity < 8:
        return "Critical Stock"


# use function for each item
for item, (quantity, price) in inventory.items():
    status = get_stock_status(quantity)
    print(item, ":", status)


# quantity_status=int(input("Enter quatity : "))
# get_stock_status(quantity_status)


# e) Save the final inventory report in a file named `store_report.txt`.
# Then print:

# * The number of **lines**
# * The number of **words** present in the file

# Also use a **regular expression** to check whether an item name contains only letters and spaces.

# ---

# ### Example Input:

# Item name: Monitor
# New quantity: 15

# ### Example Output:

# Monitor => Quantity: 15, Price: 12000

# ### Possible Report Output:

# Laptop   Stock Value = ...
# Mouse    Stock Value = ...
# Keyboard Stock Value = ...
# Monitor  Stock Value = ...
# Total Stock Value = ...
