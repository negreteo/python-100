name = input("What is your name? ")
length = len(name)
print(length)

# Create a third variable to switch values
a = input("A: ")
b = input("B: ")

c = a
a = b
b = c

print("a:", a)
print("b:", b)
