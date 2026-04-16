#Data Types
#1. Numeric Types
#a. int – Integer
#Used for quantities like item count, order number, etc.
product_quantity = 3
order_id = 10987432
print(product_quantity , order_id)

#b. float – Floating-point
#Used for prices, discounts, or ratings.

product_price = 749.99
discount_percentage = 15.5
average_rating = 4.3
print(product_price , discount_percentage , average_rating)

#c. complex – Complex Numbers
#Rarely used in e-commerce. Could be used in specialized analytics or image processing.

z = 5 + 2j # Not commonly used in typical e-commerceworkflows
print(z)

#2. Sequence Types
#a. str – String
#Used for names, addresses, categories, product descriptions, etc.

customer_name = "Rohit Sharma"
delivery_address = "Bangalore, Karnataka"
product_category = "Electronics"
print(customer_name , delivery_address)

#b. list – List
#Used to store lists of items such as products in a cart, wishlist, or categories.

cart_items = ["Shoes", "T-shirt", "Headphones"]
top_categories = ["Mobiles", "Fashion", "Home", "Beauty"]
print(cart_items , top_categories)

#c. tuple – Tuple
#Used to store fixed data, such as geographic coordinates or dimension specs (immutable).

warehouse_location = (12.9716, 77.5946) # Latitude andLongitude
product_dimensions = (12.5, 9.8, 2.2) # Length, Width,Height in inches
print(warehouse_location)

#3. Set Types
#a. set – Set
#Used to store unique items like available sizes or brands without duplicates.

available_sizes = {"S", "M", "L", "XL"}
popular_brands = {"Nike", "Adidas", "Puma", "Nike"} # 'Nike'only once
print(available_sizes)

#b. frozenset – Immutable Set
#Used when a fixed set of categories or tags should not be modified.

frozen_tags = frozenset(["Sale", "Limited Edition","Trending"])
print(frozen_tags)

#4. Mapping Type
#a. dict – Dictionary
#Used extensively to map product attributes, customer info, or order details.

product_details = {
"name": "Wireless Mouse",
"brand": "Logitech",
"price": 899.99,
"rating": 4.5}
print(product_details)

customer_profile = {
"name": "Anjali Verma",
"email": "anjali@example.com",
"prime_member": True}
print(customer_profile)

#5. Boolean Type
#a. bool – Boolean
#Used to check conditions like payment status, availability, or login status.

is_logged_in = True
is_payment_successful = False
is_in_stock = True
print(is_logged_in ,is_payment_successful  )

#6. None Type
#a. NoneType – Represents a null or missing value
#Used when something is not yet assigned, like delivery tracking not yet available.

tracking_number = None
delivery_partner = None
print(tracking_number , delivery_partner)

#Checking the Type in Python
#You can always check the type using the type() function:

print(type(product_price)) # <class 'float'>
print(type(cart_items)) # <class 'list'>
print(type(is_in_stock)) # <class 'bool'>
