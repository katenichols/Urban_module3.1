calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    count_calls()
    str_tuple = (len(string), string.upper(), string.lower())
    return str_tuple


def is_contains(string, list_to_search):
    count_calls()
    count = 0
    for i in list_to_search:
        if i.lower() == string.lower():
            count += 1
    if count > 0:
        return True
    else:
        return False


print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

print(calls)
