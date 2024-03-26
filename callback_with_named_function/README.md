# Comparing Callback with Named Function and lambda Function

## Callback with Named Function

```python
people = [
    ("John", 35),
    ("Alice", 29),
    ("Bob", 45)
]

def get_age(person):
    return person[1]

sorted_people_by_age = sorted(people, key=get_age)
```

## Callback with lambda

```python
people = [
    ("John", 35),
    ("Alice", 29),
    ("Bob", 45)
]

sorted_people_by_age = sorted(people, key=lambda person: person[1])
```
