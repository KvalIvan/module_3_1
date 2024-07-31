calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    tuple_ = (len(string), string.upper(), string.lower())
    tuple_ = list(tuple_)
    count_calls()
    print(tuple_)


def is_contains(string, list_to_search):
    list_ = []
    for i in list_to_search:
        i = i.upper()
        list_.append(i)
    string = string.upper()
    if string in list_:
        print(True)
    else:
        print(False)
    count_calls()


string_info('Capybara')
string_info('Armageddon')
is_contains('Valorant', ['ValIk', 'LOra', 'VALOraNt'])  # Urban ~ urBAN
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)
