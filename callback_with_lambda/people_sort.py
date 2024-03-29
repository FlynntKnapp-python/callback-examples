# callback_with_lambda\people_sort.py

# List of tuples (name, age)
people = [("Charlie", 35), ("Alice", 30), ("Eve", 20), ("Bob", 25), ("Diana", 40)]

print("people: ", people)

# Sort the list by age using a lambda function as the callback for the key argument
sorted_people_age = sorted(people, key=lambda person: person[1])

print("sorted_people_age: ", sorted_people_age)

# Sort the list by name using a lambda function as the callback for the key argument
sorted_people_name = sorted(people, key=lambda person: person[0])

print("sorted_people_name: ", sorted_people_name)
