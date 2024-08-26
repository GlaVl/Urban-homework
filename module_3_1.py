calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    str_info = (len(string), string.upper(), string.lower())
    return str_info


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
        if string in list_to_search:
            a = True
        else:
            a = False
    return a


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
