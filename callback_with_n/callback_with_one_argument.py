# example_01\callback_example_01.py


def callback_example(callback_function):
    callback_function()


def callback_example_n_times(callback_function, n):
    callback_function(n)


def print_the_thing():
    print("The thing!")


def print_the_other_thing():
    print("The other thing!")


def print_n_things(n):
    for _ in range(n):
        print(f"Thing {n}!")


def count_n_times(n):
    for i in range(n):
        print(i)


def print_n_first_letters_of_alpha(n):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    print(alpha[:n])


def print_n_first_fibonacci_numbers(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b


callback_example(print_the_thing)
callback_example(print_the_other_thing)


callback_example_n_times(print_n_things, 3)

callback_example_n_times(count_n_times, 5)

callback_example_n_times(print_n_first_letters_of_alpha, 7)

callback_example_n_times(print_n_first_fibonacci_numbers, 9)
