# http://www.codewars.com/kata/559ac78160f0be07c200005a/


def name_shuffler(str_):
    names_list = str_.split()
    for name in names_list:
        swap_name = names_list[1] + " " + names_list[0]

    return swap_name
