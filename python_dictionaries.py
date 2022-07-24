# check if country is in tuple and return the index, else= -1
# countries = ('USA', 'Canada', 'UK', 'France')
# your_choice_country = 'Canada'
# def find_index_by_value(value, tuple1):
#     for country in range(len(tuple1)):
#         if value == tuple1[country]:
#             return country
#     else:
#         return -1
# print(find_index_by_value(your_choice_country, countries))

countries = ('USA', 'Canada', 'UK', 'France')
your_choice_number = 8
def find_value_by_index(index, tuple1):
    if index >= 0 and index <= len(tuple1) -1:
            return tuple1[index]
    return 'No such index'
# print(find_value_by_index(your_choice_number, countries))
# add team name and city to the dictionary
new_team_name = "Wild Russia"
new_team_city = "Moscow"

nh1_hockey_teams = {
    "Canada": "Montreal",
    "Maple": "Toronto"
              }
def add_your_own_team(team_name, team_city):
   nh1_hockey_teams[team_name] = team_city

add_your_own_team(new_team_name, new_team_city)
# print(nh1_hockey_teams)
# create 2 dics and join them together
dict_1 = {
    'n'
    'ame': 'Saghi',
    'age' : 39
}
dict_2 = {
    'kid': 'Hana',
    'kid2':'Thea'
}

def join_dicts(dict1, dict2):
    dict1.update(dict2)
    return dict1

# print(join_dicts(dict_1, dict_2))
# enter a random num and generates a dict with
# keys from num to random num and value "x":x**2
number_1 = 3
def create_numbers_dict(number1):
    d = {}
    for number in range(1, number1+1):
        d[number] = number**2
    return d
# print(create_numbers_dict(number_1))
#func that adds up all values???????
dict_3 = {
    "a": 24,
    "b": 23,
    "c": 46
}
sum1 = sum(dict_3[item] for item in dict_3)
print(sum1)

#find the min and max of the countries population
dict_5 = {
    "Fiji": 898738,
    "Iran": 89878787,
    "Ukraine": 8987389988
}
def find_find_max(dict1):
    min_country = None
    min_value = None
    for key, value in dict1.items():
        if min_value is None or value <min_value:
            min_value = value
            min_country = key
    return (min_value, min_country)
# print(find_find_max(dict_5))
