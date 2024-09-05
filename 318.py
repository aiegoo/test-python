a = 100  # Initialize variable a with the value 100
result = 0  # Initialize result with 0

# Loop from 1 to 2 (inclusive)
for i in range(1, 3):
    result = a >> i  # Right shift a by i bits and assign the result to result
    result = result + 1  # Increment result by 1

print(result)  # Print the final value of result

# Output:
# 26

def func(num1, num2 = 2):
      print('a =', num1, 'b =', num2)
func(20)

# Output:
# a = 20 b = 2
