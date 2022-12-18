
def get_sqrt(number):
    # This function is not working, can you fix it?
    import math
    return math.sqrt(number)


def set_entry_checker():
    # Ask for user's data: First name, age and VIP status.
    # If user's age is under 18, do not allow user to proceed
    # If user's age is between 18 - 25, allow them to stay up to 11pm
    # If group 18_25 has more than 10 users, do not allow user to enter.
    # If user is aged over 25, welcome them without any additional conditions.
    # As an output print out the users count from each group, and also print the VIPs
    # Example input: (Georgi 28, VIP) OR (Alex 25)

    VIP_counter = 0
    group_18_25_counter = 0
    group_over_25 = 0

    name = input("What is your name ?")
    age = int(input("what is your age ?"))

    if age < 18:
        print("User is under aged")
        exit()
    elif 18 <= age <= 25:
        if group_18_25_counter < 10:
            group_18_25_counter += 1
        else:
            print("No more capacity")

    else:
        group_over_25 += 1
    vip_status = input("Are you a VIP ?")
    if vip_status == "VIP":
        VIP_counter += 1

    print(f"{group_18_25_counter} group 18-25")
    print(f"{group_over_25} group 25+")
    print(f"{VIP_counter} are the VIP")


def get_even_numbers(array):
    # Finish the function by adding code that would print out only the even numbers.
    array_even = []
    for n in array:
        if n % 2 == 0:
            array_even.append(n)
    print(array_even)


def reverse_words_from_string(input_string):
    """
       Given a string , reverse words.
       Example:
       Input : Today is our Python exercises with group one from strypes-04 course.
       Output: course. strypes-04 from one group with exercises Python our is Today
       :param string:
       :return: reversed string
    """
    words = input_string.split()
    reversed_words = reversed(words)
    reversed_string = " ".join(reversed_words)
    return reversed_string


def get_is_password_valid():
    # Ask for user's password.
    # Check user's password against the following conditions:
    # At least 6 symbols, and maximum of 32 symbols.
    # At least 1 upper case letter.
    # At least 1 symbol.
    # hint: use the re library.
    import re



    password = input("What is your password ?")
    pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,32}$"
    if not re.match(pattern, password):
        return False
    return True                            #predpolagam moje da stane na edin red
                                            # return re.match(pattern,password)
                                            # mashinata ne mi importva re i go testvam onlie i nz dali e okey




def reversed_integer(number):
    """
        Given an integer, return the integer with reversed digits.
        Note: The integer could be either positive or negative.
        Example:
        Input : -258
        Output: -852
        :param number:
        :return: reversed number
    """

    if number < 0:
        number_s = str(number)
        new_number_s = number_s[1:]


        reversed_s = new_number_s[::-1]
        with_minus = "-" + reversed_s
    else:
        number_as_string = str(number)
        rev_numb = number_as_string[::-1]
        return rev_numb

    return with_minus



def is_perfect_number(num):
    """
        Write a Python function to check whether a number is perfect or not.
        According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of
        its proper positive divisors, that is, the sum of its positive divisors excluding the number itself
        (also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum of all
        of its positive divisors (including itself).
        Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6
        Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6.
        The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128
        Input : 6
        Output: True
        :param number:
        :return: is perfect or not?
    """

    sum = 0

    for n in range(1,num):
        if num % n == 0:
            sum += n

    return print((sum == num))

def find_first_unique_character(string):
    """
    Write a Python function which find index of first unique character from string.
    Given a string, find the first non-repeating character in it and return its index.
    If it doesn't exist, return -1. # Note: all the input strings are already lowercase.
    Input: abcdcaf
    Output: 1 (we return 1 because b is the first non-repeating char at index 1 in the string "abcdcaf")
    :param string:
    :return: first unique character
    """

    pass

def find_count_match_words_from_list(words):
    """
    Write a Python function to count the number of words where the length > 2 and the first and last character
    are same from a given list of words(strings)
    Input: ['abc', '121', 'def', 'level'] -> 121, level
    Output: 2
    :param words:
    :return: number of match words
    """

    pass