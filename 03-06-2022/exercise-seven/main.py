def fibonacci(number: int) -> list:
  a, b = 0, 1
  result = []

  while a < number:
    result.append(a)
    a, b = b, a+b

  return result

print(fibonacci(number=100))
