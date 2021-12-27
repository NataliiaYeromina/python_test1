import random
from random import randint


def list_str_task_1(some_list):
    new_list = []
    for word in some_list:
        if word[0] == "a":
            new_list.append(word)
    return new_list


def list_str_task_2(some_list_srt):
    new_list_str = []
    for word in some_list_srt:
        if "a" in word:
            new_list_str.append(word)
    return new_list_str


def list_task_3(some_list):
    new_list_str = []
    for ind in some_list:
        if type(ind) == str:
            new_list_str.append(ind)
    return new_list_str


def return_letter_str_task_4 (some_string):
    new_list = []
    for elem in some_string:
        if some_string.count(elem) == 1:
            new_list.append(elem)
    return new_list
#
#
def common_elem_str(some_str_1, some_str_2):
    new_str = []
    for elem in some_str_1:
        if elem in some_str_2:
            new_str.append(elem)
    return list(set(new_str))



def common_elem_onceintwostr (some_str_1,some_str_2):
    elem_once_in_str_1 = return_letter_str_task_4(some_str_1)
    elem_once_in_str_2 = return_letter_str_task_4(some_str_2)
    common_elem = common_elem_str(elem_once_in_str_1,elem_once_in_str_2)
    return common_elem


def create_email(name,domain):
    number = random.randint(100,999)
    random_name = random.choice(name)
    random_word = ''.join(chr(randint(ord('a'), ord('z'))) for j in range(randint(5, 7)))
    random_domain = random.choice(domain)
    email = f"{random_name}.{number}@{random_word}.{random_domain}"
    return email



my_list = ["fox", "apple","butterfly","ant","arrow","pen","allo"]
result_task_1 = list_str_task_1(my_list)
print(result_task_1)

my_list_2 = ["asd","sca","x","axc","ta","a"]
result_task_2 = list_str_task_2(my_list_2)
print(result_task_2)

my_list_3 = [12,"as",5,"kj","11",6,"f",8]
result_list_str_task_3 = list_task_3(my_list_3)
print(result_list_str_task_3)

my_str = "qqweeerrty"
result_task_4 = return_letter_str_task_4(my_str)
print(result_task_4)

our_str_1 = "qqwwerrttyy"
our_str_2 = "qweeeeeee123"
result_task_5 = common_elem_str(our_str_1, our_str_2)
print(result_task_5)

str_1 = "qwwwwerrrrtyyyy"
str_2 = "qweeeeeeerty123"
result_task_6 = common_elem_onceintwostr(str_1,str_2)
print(result_task_6)


names = ["anna",'amina','sveta','tanya',"nata"]
domains = ['kk','ua','vv','xxx']
e_mail = create_email(names,domains)
print(e_mail)




