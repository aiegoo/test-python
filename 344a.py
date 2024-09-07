# Define a list of lists `a` with two sublists
a = [[1, 1, 0, 1, 0], [1, 0, 1, 0]]

# Initialize `tot` and `totsu` to 0
tot, totsu = 0, 0

# Iterate over each sublist `i` in the list `a`
for i in a:
    # Iterate over each element `j` in the sublist `i`
    for j in i:
        # Add `j` to `tot`
        tot += j
    # Add the length of the sublist `i` to `totsu`
    totsu += len(i)

# Print the values of `tot` and `totsu`
print(tot, totsu)

# What is the output of this code?
# a) 5 3
