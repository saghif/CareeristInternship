# enter a random number and multiply each digit
product = 1
number_1 = 1234
string_2 = str(number_1)
for digit in string_2:
    int_digit = int(digit)
    product *= int_digit
# print(product)

# enter random number and reverse numbers
random_num = 1234
string = str(random_num)
result_3 = string[::-1]
result_3 = int(result_3)
# print(result_3, type(result_3))

list_1 = [1, 'asdsd', True, 2, False, 4, 'Hello', None, range(1, 11), 100]


def swap_first_last(array_1):
    array_1[0], array_1[-1] = array_1[-1], array_1[0]
    return array_1


# print(swap_first_last(list_1))


list_2 = [1, 'asdsd', True, 2, False, 4, 'Hello', None, range(1, 11), 100]


def reverse_list(array_2):
    array_2.reverse()
    return array_2


# print(reverse_list(list_2))

# create list of nums and multiply all items
list_3 = [1, 2, 3, 4, 5]


def multiply_list_items(array_3):
    total = 1
    for items in array_3:
        total = total * items
    return total


# print(multiply_list_items(list_3))

# create list and find smallest num
list_4 = ['hd', 'hkjhs', 36, 78, 2, 3, -1]


def smallest_item_list(all_nums):
    all_nums = min(all_nums)
    return all_nums


# print(smallest_item_list(list_4))

# remove duplicates
list_5 = [1, 2, 3, 1, 1, 1, 2, 3, 4, 'hello', 1, 2, 3, 4, 'hello']


def remove_duplicates_list(array_5):
    unique_values = []
    for value in array_5:
        if value not in unique_values:
            unique_values.append(value)
    return unique_values


# print(remove_duplicates_list(list_5))

# enter a digit and return list of words that are longer than the dig

number_1 = 5
list_6 = ['on', 'ifd', 'saghi', 'hanicka', 'thea', 'jhksasjasjas']
def longer_words_list(array_6, number1):
    new_list5 = []
    for words in array_6:
        if len(words) > number1:
            new_list5.append(words)
    return new_list5
# print(longer_words_list(list_6, number_1))

# Return true if there is one common
list_7 = [1, 2, 3, 4, 5, 6, 'hello']
list_8 = ['no', 'yes', 'hello', 2, 3]


def find_item_lists(array_7, array_8):
    for items in array_7:
        if items in array_8:
            return True
    return False
# print(find_item_lists(list_7, list_8))

#make string

list_9 = ['I', ' ', 'like']

def string_version(array_14):
    # the function way :
    # return ''.join(array_14)
    new_string = ""
    for items in array_14:
        new_string += items
    return new_string
# print(string_version(list_9))


list_10 = [1, 2, 3, 1, 3, 3, 3]
number_2 = 3
def count_items_list(array_10, number2):
    return array_10.count(number2)
# print(count_items_list(list_10, number_2))

# bring back the even numbers
list_11 = [2, 6, 7, 8, 10, 14, 19, 23]

def even_numbers_list(array_11):
    even_list = []
    for items in array_11:
        if items % 2 == 0:
            even_list.append(items)
    return even_list
# print(even_numbers_list(list_11))





