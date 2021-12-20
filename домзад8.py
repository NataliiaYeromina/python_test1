from random import randint


def value_int_task_1 ():
    rand_int = randint(1,100)
    print(rand_int)

def value_int_task_2 ():
    rand_int = randint(1,100)
    return rand_int

def value_int_task_3 ():
    rand_int = randint(1, 100)
    if rand_int > 50:
        print("Хорошо")
    else:
        print("Плохо")

def str_upper_task_4 (some_string):
    print(some_string.upper())

def str_upper_return_task_5 (some_string):
    return some_string.upper()

def list_str_task_6 (list_str):
    new_list_str = []
    for word in list_str:
        new_list_str.append(word.upper())
    return new_list_str

def return_list_int_task_7(value_int):
    my_range = []
    for one_int in range(1, value_int + 1):
        my_range.append(one_int)
    return my_range

def calculate_task_8(value_int):
    our_list = []
    first_int = 1
    while first_int ** 2 <= value_int:
        our_list.append(first_int ** 2)
        first_int += 1
    return our_list



value_int_task_1()

result_2 = value_int_task_2()
print(result_2)

value_int_task_3()


our_str = "Привет всем"
str_upper_task_4(our_str)


our_str = "upPerCase"
result_5 = str_upper_return_task_5(our_str)
print(result_5)


our_list_str = ["hello","world","python","java"]
result_6 = list_str_task_6(our_list_str)
print(result_6)


our_int = 9
result_7 = return_list_int_task_7(our_int)
print(result_7)


our_value_int = 225
result = calculate_task_8(our_value_int)
print(result)