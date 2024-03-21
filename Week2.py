my_list = []  # Create an empty list called my_list.
my_list.append("10")  # Append the element '10' to my_list.
my_list.append("20")  # Append the element '20' to my_list.
my_list.append("30")  # Append the element '30' to my_list.
my_list.append("40")  # Append the element '40' to my_list.
print("Initial:", my_list)

my_list.insert(1, "15")  # Insert the value '15' at the second position in the list (index 1).
print("Amended:", my_list)
my_list.extend(["50", "60", "70"])  # Extend my_list with another list: [50, 60, 70].
print("Amend1:", my_list)
my_list.pop()  # Remove the last element from my_list.
print("Amend 2:", my_list)
my_list.sort()  # Sort my_list in ascending order.
print("Amend3:", my_list)
index_of_30 = my_list.index("30")  # Find the index of the value '30' in my_list.
print("Index of '30':", index_of_30)  # Print the index of '30' in my_list.
