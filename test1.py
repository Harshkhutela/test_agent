class Calculator:

    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_sum(self):
        total = 0
        for n in self.numbers:
            total += n   
        return total

    def print_length(self):
        print("Length:", len(self.numbers))


data = {"a": 10, "b": 20}
print("Value of c:", data.get("c", "Key not found"))

num = '5'
try:
    num = int(num) or 5
except ValueError:
    print("Invalid input")
print("Number:", num)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial:", factorial(5))

i = 0
while i < 5:
    print("Looping...")
    i += 1

calc = Calculator([2, 3, 4])
print("Sum:", calc.calculate_sum())
calc.print_length()