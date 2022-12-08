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
        transactions_even.append(transaction_id)
        return transactions

print(store_transactions(2,transactions_even))

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
    import pprint
    dict = {
        "level1": {
            "attr1": "value",
            "attr2": "value",
            "level2": {
                "attr1": "value",
                "attr2": "value",
                "level3": {
                    "attr1": "value",
                }
            }
        }
    }



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
    calcs.append(sum)
    calcs.append(subtract)
    calcs.append(product)
    calcs.append(reminder)

    return calcs

print(store_calcs(2,3,calcs_array))

def get_chars_count(string):
    """
    :param string:
    :return: dict holding string chars count with and without counter
    """
    dictt = {string: len(string)}
    return dictt

print(get_chars_count("pezi"))


def get_abbreviation(string):
    """
    :param string:
    :return: abbreviation from the string (first 3 symbols).
    If string is shorter than 5 chars, return it all.
    """
    if len(string) < 5:
        return string
    else:
        return string[0::3]

print(get_abbreviation("pezzzziii"))

def get_titled_string(sentence):
    """
    :param sentence:
    :return: Return a titled and lower version of the sentence
    """

    return sentence.title(), sentence.lower()

print(get_titled_string("asdda"))


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
                new_arr.append(array[i])
                new_arr.append(array[j])
                return new_arr

arr1 = [1,2,3,11,4]

print(get_number_sum(arr1,4))


arr1 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

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
    arr_idx = 0
    seq_idx = 0
    while arr_idx < len(array) and seq_idx < len(sequence):
        if array[arr_idx] == sequence[seq_idx]:
            seq_idx += 1
        arr_idx += 1
    return seq_idx == len(sequence)


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(get_is_valid_subsequence(array, sequence))



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

    return False



