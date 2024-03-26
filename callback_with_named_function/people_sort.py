# Sorting with a callback
print("\nSorting with a lambda callback:")
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

# The lambda function here is a simple callback function that helps sorted() understand how to sort the tuples
# in the people list.
# The lambda function takes a person tuple as input and returns the second element of the tuple (the age).
# This tells sorted() to sort the people list based on the age of each person.
# The sorted() function uses the lambda function as a callback to determine the sorting order.
# The key argument specifies the callback function to use for sorting.
# The lambda function `person: person[1]` is the callback function that returns the second element of the person tuple.
#
sorted_people_by_age = sorted(people, key=lambda person: person[1])

print("People sorted by age:", sorted_people_by_age)


# Explicit callback function
print("\nSorting with an named callback function:")


def get_age(person):
    return person[1]


sorted_people_by_age = sorted(people, key=get_age)

print("People sorted by age:", sorted_people_by_age)
