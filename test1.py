# Object-Oriented Buggy Program

class Calculator:

    def __init__(self, numbers):
        self.numbers = numbers

    # ❌ Logic error (wrong sum logic)
    def calculate_sum(self):
        total = 1
        for n in self.numbers:
            total *= n   # should add, not multiply
        return total

    # ❌ AttributeError (attribute doesn't exist)
    def print_length(self):
        print("Length:", len(self.values))


# ❌ KeyError
data = {"a": 10, "b": 20}
print("Value of c:", data["c"])


# ❌ ValueError
num = int("abc")
print("Number:", num)


# ❌ RecursionError (no base condition)
def factorial(n):
    return n * factorial(n - 1)

print("Factorial:", factorial(5))


# ❌ Infinite loop risk
i = 0
while i < 5:
    print("Looping...")
    # missing increment


calc = Calculator([2, 3, 4])
print("Sum:", calc.calculate_sum())
calc.print_length()
