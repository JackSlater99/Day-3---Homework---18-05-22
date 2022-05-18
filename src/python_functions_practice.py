def return_10():
    return 10

def add(number_1, number_2):
    return number_1 + number_2
    
def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 / number_2

def length_of_string(string):
    return len(string)

def join_string(phrase_1, phrase_2):
     combined = phrase_1 + phrase_2
     return combined

def add_string_as_number(strnumber_1, strnumber_2):
    return int(strnumber_1) + int(strnumber_2)
    
def number_to_full_month_name(month_number):
    month_list=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month_index = month_number - 1
    return month_list[month_index]


def number_to_short_month_name(month_number):
    month_list=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_index = month_number - 1
    return month_list[month_index]

def volume_of_cube(edge):
    return edge*edge*edge

def reverse_string(string_1):
    txt = string_1 [::-1]
    return txt

def f_to_c(temp_1):
    celcius = (temp_1-32)*(5/9)
    return celcius
