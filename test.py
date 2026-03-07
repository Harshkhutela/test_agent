# Buggy Python Program for Testing

numbers = [10, 20, 30, 40]

total = 0

# ❌ IndexError
for i in range(6):
    total += numbers[i]

print("Total:", total)

# ❌ ZeroDivisionError
x = 50
y = 0
result = x / y
print("Division:", result)

# ❌ NameError (count not defined)
average = total / count
print("Average:", average)

# ❌ TypeError (len on None)
data = None
print("Length:", len(data))

# ❌ SyntaxError (missing colon)
if total > 50
    print("Large total")

# ❌ Logical error
radius = 5
area = 2 * 3.14 * radius
print("Area:", area)

# ❌ Blocking input (automation issue)
name = input("Enter your name: ")
print("Hello", username)
