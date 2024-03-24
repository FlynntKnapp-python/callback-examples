# example_01\callback_example_01.py


def callback_example(callback_function):
    """
    Calls the callback function.

    Args:
        callback_function: The function to call.

    Returns:
        None
    """
    callback_function()


def callback_example_with_one_arg(callback_function, n):
    """
    Calls the callback function with one argument.

    Args:
        callback_function: The function to call.
        n: The argument to pass to the callback function.

    Returns:
        None
    """
    callback_function(n)


def print_the_thing():
    """
    Prints 'The thing!'

    Returns:
        None
    """
    print("The thing!")


def print_the_other_thing():
    """
    Prints 'The other thing!'
    Returns:
        None
    """
    print("The other thing!")


def print_n_things(n):
    """
    Prints 'Thing n!' n times.

    Args:
        n: The number of times to print 'Thing n!'

    Returns:
        None
    """
    for _ in range(n):
        print(f"Thing {n}!")


def count_n_times(n):
    """
    Prints numbers from 0 to n.

    Args:
        n: The number of times to print numbers.

    Returns:
        None
    """
    for i in range(n):
        print(i)


def print_n_first_letters_of_alpha(n):
    """
    Prints the first n letters of the alphabet.

    Args:
        n: The number of letters to print.

    Returns:
        None
    """
    alpha = "abcdefghijklmnopqrstuvwxyz"
    print(alpha[:n])


def print_n_first_fibonacci_numbers(n):
    """
    Prints the first n Fibonacci numbers.

    Args:
        n: The number of Fibonacci numbers to print.

    Returns:
        None
    """
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b


def print_n_first_prime_numbers(n):
    pass


# Call the callback_example function with different callback functions
# as arguments.
# There are no arguments being passed to the callback functions.
callback_example(print_the_thing)
callback_example(print_the_other_thing)

# Call the callback_example_with_one_arg function with different callback functions
# as arguments.
# The callback functions take one argument.

# The first argument is the callback function: print_n_things
# The second argument is the argument to pass to the callback function: 2
callback_example_with_one_arg(print_n_things, 2)

# The first argument is the callback function: count_n_times
# The second argument is the argument to pass to the callback function: 3
callback_example_with_one_arg(count_n_times, 3)

# The first argument is the callback function: print_n_first_letters_of_alpha
# The second argument is the argument to pass to the callback function: 4
callback_example_with_one_arg(print_n_first_letters_of_alpha, 4)

# The first argument is the callback function: print_n_first_fibonacci_numbers
# The second argument is the argument to pass to the callback function: 5
callback_example_with_one_arg(print_n_first_fibonacci_numbers, 5)
