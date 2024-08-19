firstValue: float = float(input("Enter with a value: "))
secondValue: float = float(input("Enter with another value: "))

operation: str = input(
    "Enter with the type of operation:\n+ for addition\n- for subtraction\n* for multiplication\n/ for division\n** for potenciation\n% for module\nOption selected: "
)

def addition(firstValue: float, secondValue: float) -> float:
  return firstValue + secondValue

def subtraction(firstValue: float, secondValue: float) -> float:
  return firstValue - secondValue

def multiplication(firstValue: float, secondValue: float) -> float:
  return firstValue * secondValue

def division(firstValue: float, secondValue: float) -> float:
  if secondValue == 0:
    return firstValue
  return firstValue / secondValue

def potenciation(firstValue: float, secondValue: float) -> float:
  return firstValue ** secondValue

def module(firstValue: float, secondValue: float) -> float:
  if secondValue == 0:
    return firstValue
  return firstValue % secondValue

match (operation):
  case "+":
    print(addition(firstValue, secondValue))
  case "-":
    print(subtraction(firstValue, secondValue))
  case "*":
    print(multiplication(firstValue, secondValue))
  case "/":
    print(division(firstValue, secondValue))
  case "**":
    print(potenciation(firstValue, secondValue))
  case "%":
    print(module(firstValue, secondValue))
  case _:
    print("Invalid operation! Try again.")
