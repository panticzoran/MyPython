# Creating Pure Function that calculates the total price of items in a shopping cart, 
# considering the price and quantity of each item

def calculateTotal(cartItems):
  return sum(item['price'] * item['quantity'] for item in cartItems)

# Example of cart items
cart = [
  {"name": "Apple", "price": 0.5, "quantity": 4},
  {"name": "Orange", "price": 0.3, "quantity": 7},
  {"name": "Banana", "price": 0.2, "quantity": 10}
]

print("The cart has following items: ", cart, "\n")
print("The total:", calculateTotal(cart))