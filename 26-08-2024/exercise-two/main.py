values: list[int] = []
print(values)

for _ in range(5):
  value = int(input("Enter an integer value: "))
  # Add element in the end of the list
  values.append(value)
  print(values)

weekDays: list[str] = ["Sunday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(weekDays)
# Add "Monday" in the index number one on the list
weekDays.insert(1, "Monday")
print(weekDays)
# Add "Tuesday" in the index number two on the list
weekDays.insert(2, "Tuesday")
print(weekDays)

# Remove the element called "Monday" of the list.
# It will remove the first element that matches the value.
weekDays.remove("Monday")
print(weekDays)

# Remove a specific element from the list.
weekDays.pop(0)
print(weekDays)

print("Tuesday" in weekDays) # True
print("Tuesday" not in weekDays) # False
