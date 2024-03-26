# example_01\callback_example_01.py


def callback_example(callback_function):
    """
    Calls the callback function.

    Args:
        callback_function: The function to call.

    Returns:
        None
    """
    return callback_function()


def callback_example_with_one_arg(callback_function, n):
    """
    Calls the callback function with one argument.

    Args:
        callback_function: The function to call.
        n: The argument to pass to the callback function.

    Returns:
        None
    """
    return callback_function(n)


def return_the_thing():
    """
    Returns 'The thing!'

    Returns:
        str: The string 'The thing!'
    """
    return "The thing!"


def return_the_other_thing():
    """
    Returns 'The other thing!'
    Returns:
        str: The string 'The other thing!'
    """
    return "The other thing!"


def return_n_things(n):
    """
    Returns list with 'Thing!' n times.

    Args:
        n: The number of 'Thing!'s in the list

    Returns:
        list: A list with 'Thing!' n times.
    """
    # Use a list comprehension to create the list.
    return [f"Thing!" for _ in range(n)]

    # Alternatively, you can use a for loop to create the list.
    # things = []
    # for _ in range(n):
    #     things.append(f"Thing {n}!")
    # return things

    # for _ in range(n):
    #     print(f"Thing {n}!")


def return_n_numbers(n):
    """
    Returns numbers from 0 to n-1.

    Args:
        n: The number of numbers to return.

    Returns:
        list: A list of numbers from 0 to n-1.
    """
    return [i for i in range(n)]


def return_n_letters(n):
    """
    Returns a list of the first n letters of the alphabet.

    Args:
        n: The number of letters to return.

    Returns:
        list: A list of the first n letters of the alphabet.
    """
    alpha = "abcdefghijklmnopqrstuvwxyz"
    return [alpha[i] for i in range(n)]


def return_first_n_fibonacci_numbers(n):
    """
    Returns a list of the first n Fibonacci numbers.

    Args:
        n: The number of Fibonacci numbers to return.

    Returns:
        list: A list of the first n Fibonacci numbers.
    """
    # a, b = 0, 1
    # for _ in range(n):
    #     print(a)
    #     a, b = b, a + b

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


def return_first_n_prime_numbers(n):
    """
    Returns a list of the first n prime numbers.

    Args:
        n: The number of prime numbers to return.

    Returns:
        list: A list of the first n prime numbers.
    """
    pass


# Call the callback_example function with different callback functions
# as arguments.
# There are no arguments being passed to the callback functions.
the_thing = callback_example(return_the_thing)
print("the_thing: ", the_thing)
the_other_thing = callback_example(return_the_other_thing)
print("the_other_thing: ", the_other_thing)

# Call the callback_example_with_one_arg function with different callback functions
# as arguments.
# The callback functions take one argument.

# The first argument is the callback function: print_n_things
# The second argument is the argument to pass to the callback function: 2
two_things = callback_example_with_one_arg(return_n_things, 2)
print("two_things: ", two_things)

# The first argument is the callback function: count_n_times
# The second argument is the argument to pass to the callback function: 3
three_numbers = callback_example_with_one_arg(return_n_numbers, 3)
print("three_numbers: ", three_numbers)

# The first argument is the callback function: print_n_first_letters_of_alpha
# The second argument is the argument to pass to the callback function: 4
four_letters = callback_example_with_one_arg(return_n_letters, 4)
print("four_letters: ", four_letters)

# The first argument is the callback function: print_n_first_fibonacci_numbers
# The second argument is the argument to pass to the callback function: 5
first_five_fib = callback_example_with_one_arg(return_first_n_fibonacci_numbers, 5)
print("first_five_fib: ", first_five_fib)
