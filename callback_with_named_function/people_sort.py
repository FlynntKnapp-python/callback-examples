# Sorting with a callback
print("\nSorting with a lambda callback")
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

# The lambda function here is a simple callback function that helps sorted() understand how to sort the tuples
sorted_people_by_age = sorted(people, key=lambda person: person[1])

print("People sorted by age:", sorted_people_by_age)


# Explicit callback function
print("\nSorting with an named callback function")


def get_age(person):
    return person[1]


sorted_people_by_age = sorted(people, key=get_age)

print("People sorted by age:", sorted_people_by_age)
