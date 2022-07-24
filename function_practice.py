# calculate the difference
def difference(num_1, num_2):
    diff = num_1 - num_2
    return diff


# print(difference(10, 5))

# divide 2 nums
def division(num_1, num_2):
    result = num_1 / num_2
    return result
# print(division(8, 4))

# gets random num, if more than 10 = 100- num, if less than 10 = num x 10
def random_num(num):
    if num > 10:
        result = 100 - num
        return result
    else:
        result = num * 10
        return result
# print(random_num(8))


def temperature_convertor(temp):
   result = (temp - 32) * 5/9
   return result
# print(temperature_convertor(70))
# taxifare calculation:
def taxi_fare(distance):
    distance = distance * 1000
    per_meter = distance / 140
    fare_calculation = (per_meter * 0.25) + 4.00
    return fare_calculation
# print(round(taxi_fare(10), 2))
#removing vowels
def no_vowels(string):
    vowels = 'aeiouaAEIOU'
    new_string = ''
    for char in string:
        if char not in vowels:
            new_string = new_string + char
    return new_string

# print(no_vowels('hello world'))

# number pyramids
# print("Number Pattern ")

# Decide the row count. (above pattern contains 5 rows)
row = 5
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop 5 times
# for i in range(1, row + 1, 1):
#     # Run inner loop i+1 times
#     for j in range(1, i + 1):
# print(j, end=' ')
    # empty line after each row
    # print("")
# sum = 1
# entered_num = input('Enter a numer: ')
# for x in range(1, entered_num +1):
#     for j in range():
a_number = input('Enter the number: ')
a_number = int(a_number)
def multi_eleven(s):
    if s % 11 == 0:
        return 'Yes'
    else:
        return 'No'
print(multi_eleven(a_number))




