matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in matrix:
  for j in i:
    print(j, end=" ")
  print()

print("Matrix length:", len(matrix))

matrix.append([10, 11, 12])

secondMatrix: list[list[int]] = [[13, 14, 15]]
joinMatrix: list[list[int]] = matrix + secondMatrix
print(joinMatrix)
