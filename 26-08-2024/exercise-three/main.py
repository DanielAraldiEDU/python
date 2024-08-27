number: float = float(input("Enter a number: "))

type = None

type = "even" if number % 2 == 0 else "odd"

match type:
  case "even":
    print("The number is even")
  case "odd":
    print("The number is odd")
  case _:
    print("Invalid type")

while number != 0:
  number = float(input("Enter a number: "))
  print(number)
print("Exit while")
