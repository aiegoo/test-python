# Get the number of elements from the user
x = int(input("Enter the number of elements: "))

# Get the elements from the user and append them to the array
for i in range(x):
  element = input("Enter element {}: ".format(i+1))
  my_array.append(element)

# Remove an element from the array
element_to_remove = input("Enter the element to remove: ")
if element_to_remove in my_array:
  my_array.remove(element_to_remove)
  print("Element removed successfully!")
else:
  print("Element not found in the array.")

# Generate a range of numbers and append them to the array
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
step = int(input("Enter the step size: "))

for num in range(start, end, step):
  my_array.append(num)
  # Convert the input values to strings
  my_array = [str(value) for value in my_array]

  # Print the array elements
  print("Array elements:", my_array)

  # Sort the array in ascending order
  my_array.sort()
  print("Sorted array:", my_array)

  # Reverse the array
  my_array.reverse()
  print("Reversed array:", my_array)

  # Find the index of an element in the array
  element_to_find = input("Enter the element to find: ")
  if element_to_find in my_array:
    index = my_array.index(element_to_find)
    print("Element found at index:", index)
  else:
    print("Element not found in the array.")

  # Count the occurrences of an element in the array
  element_to_count = input("Enter the element to count: ")
  count = my_array.count(element_to_count)
  print("Element count:", count)

  # Clear the array
  my_array.clear()
  print("Array cleared:", my_array)
