my_list = []
my_list.append(10,)
my_list.append(20)
my_list.append(30)      
my_list.append(40)
my_list.insert(1, 15)  # Insert 15 at index 2

list = [50, 60, 70]
my_list.extend(list)  # Extend my_list with elements from list
my_list.remove(70)  # Remove the first occurrence of 70
my_list.sort()  # Sort the list in ascending order

index_of_30 = my_list.index(30)  # Get the index of the first occurrence of 30
print(index_of_30)
print(my_list)
