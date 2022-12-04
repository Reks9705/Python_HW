def print_student_sentence(name, age, today):
    """
    :param name:
    :param age:
    :param today:
    :return: None
    """
    # Write code that prints out a sentence like
    # <name> is aged <age>. He is a passionate learner, and he started a JD program just <today>

    print(f"{name} is aged {age}. He is a passionate learner, and he started a JD program just {today}")


transactions_even = []


def store_transactions(transaction_id, transactions):
    """
    :param transaction_id:
    :param transactions: transactions_even
    :return: transactions
    """
    # Write code that stores the transaction_id if it is an even number
    # The function should return the transactions
    if transaction_id % 2 == 0:
        return transactions


def pretty_print_dict(dictionary):
    """
    :param dictionary:
    :return: NOne
    If we have the following dictionary
    {
        level1: {
            attr1: value,
            attr2: value,
            level2: {
                attr1: value,
                attr2: value,
                level3: {
                    attr1: value,
                }
            }
        }
    }
    The desired output is the dictionary data printed in a pretty manner - tabulated (4 tabs) per
    level
    """
    [print(key, ":", value) for key, value in dictionary.items()]


calcs_array = []


def store_calcs(number1, number2, calcs):
    """
    Write a code that stores the sum, subtract, product and reminder
    of number1 and number2 within calcs_array
    :param number1:
    :param number2:
    :param calcs: calcs_array
    :return: calcs
    """
    sum = number1 + number2
    subtract = number1 - number2
    product = number1 * number2
    reminder = number1 % number2
    calcs_array = [sum, subtract , product, reminder]

    return calcs


def get_chars_count(string):
    """
    :param string:
    :return: dict holding string chars count with and without counter
    """
    dict = {string: len(string)}
    return dict


def get_abbreviation(string):
    """
    :param string:
    :return: abbreviation from the string (first 3 symbols).
    If string is shorter than 5 chars, return it all.
    """
    if len(string) < 5:
        return string
    else:
        return get_abbreviation(string)

def get_titled_string(sentence):
    """
    :param sentence:
    :return: Return a titled and lower version of the sentence
    """

    return get_titled_string(sentence), sentence.lower()


def get_number_sum(array, target_sum):
    """
    Example:
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    target_sum = 10
    result = [-1, 11]
    :param array: Non-empty array of integers
    :param target_sum: integer
    :return: new array holding 2 numbers which sum = target_sum. If no such numbers, return []
    """

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target_sum:
                new_arr = []
                return new_arr[i, j]



def get_is_valid_subsequence(array, sequence):
    """
    Given two non-empty arrays of integers, finish the function by adding code that determines if
    the second array is a subsequence of the first one.
    Subsequence is not mandatory adjacent in the array, but following the same order.
    Example:
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    result: True
    :param array:
    :param sequence:
    :return: bool
    """

    pass


def get_is_palindrome(string):
    """
    Finish the function by adding code that returns a boolean with palindrome check.
    A string is palindrome if it is written the same forward and backward. Single char string is
    a palindrome string.
    Example:
    string = 'abcdcba'
    result: True
    :param string:
    :return: bool
    """

    if string == string[::-1]:
        return True
    else:
        return False


print_student_sentence("Galin", 25, 22.07)


store_transactions(2, 13)


store_calcs(4, 1, 1)

get_chars_count("pezi")

dict = {"1": "a", "2": "b", "3": "c"}

pretty_print_dict(dict)