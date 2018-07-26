def screen_markdown(string):
    special_symbols = ['*', '_', '[']
    new_string = ''

    for char in string:
        if char in special_symbols:
            new_string += '\\'
        new_string += char

    return new_string


def italic(string):
    return '_' + string + '_'


def bold(string):
    return '*' + string + '*'


def code(string):
    return '`' + string + '`'
