firstValue: float = float(input("Enter with a value: "))
secondValue: float = float(input("Enter with another value: "))

print("---------")
print(firstValue)
print(secondValue)
print("---------")

firstValue, secondValue = secondValue, firstValue

print("---------")
print(firstValue)
print(secondValue)
print("---------")

integer: int = 1
print(integer)
number: float = 1.0
print(number)
boolean: bool = True
print(boolean)
listOfCars: list = ["Ford", "Volvo", "BMW"]
print(listOfCars)
# A tuple is a constant list that cannot be changed
tupleOfCars: tuple = ("Ford", "Volvo", "BMW")
print(tupleOfCars)
rangeOfCars = range(len(listOfCars))
print(rangeOfCars)
