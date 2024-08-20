print("Computer" + " Science", "\n")
print("Computer Science\n" * 10)

surname: str = "Braz"
name: str = "Waldir %s" % (surname)
print(name, "\n")

listOfNames: list[str] = ["Waldir", "José", "Maria"] * 10
print(listOfNames, "\n")

print(listOfNames[0], "\n")

matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix, "\n")

for index in range(len(listOfNames)):
  print(listOfNames[index])
