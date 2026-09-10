#Global Freight Calculator


Sender_name = input("Sender's the name -----> ")
Type_of_item = input("What is the item being shipped? -----> ")
is_Fragile = bool(input("Is thy Item fragile? -----> "))
weight = float(input("What is the weight of the item? -----> "))
distance = float(input("What is the distance of thy home? ------> "))
is_express = bool(input("Is the order a express order? ------> "))
is_international = bool(input("Is the order an international order? ------> "))

print("The name is", Sender_name)
print("The item being shipped is", Type_of_item)

if is_Fragile == 'True':
    print("We will notify thy carrier.")
else:
    print("Thank the for answering.")

print("The weight of the item is", weight, "kg")
print("The distance of the place is", distance, "km")

base_cost = (weight * 2.50) + (distance * 0.15)

Total1 = (base_cost * 1.40) + 50
Total2 = (base_cost * 1.20) + 25
Total3 = (base_cost + 30)
Total4 = (base_cost)

if weight <= 2.0 and distance <= 100 and is_international == 'False' and is_express == 'False':
    print("You have free shipping for this item.")
