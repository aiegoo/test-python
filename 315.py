class Cls:
    # Class-level variables x and y are initialized to 10 and 20 respectively
    x, y = 10, 20

    def chg(self):
        # Store the value of self.x in a temporary variable temp
        temp = self.x
        # Assign the value of self.y to self.x, effectively swapping the values
        self.x = self.y
        # Assign the value stored in temp (original self.x) to self.y, completing the swap
        self.y = temp

# print(a.x, a.y)
a = Cls()
print(a.x, a.y)
a.chg()
print(a.x, a.y)

# print(a.x, a.y)

