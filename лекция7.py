# 1. Дано целое число (int). Определить сколько нулей в этом числе.
# number = 1200300400
# number = str(number)
# my_symbol = "0"
# result = number.count(my_symbol)
# print(result)

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа.
# Например для числа 1002000 - три нуля
# n = 1002000
# c = 0
# while n%10==0:
#      c +=1
#      n//=10
# print(c)

# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.

# a = ['hi','hello',"apple","cat"]
# b = []
# for c in range(len(a)):
#     if c % 2 != 0:
#         l = a[c]
#         b.append(l[::-1])
#     else:
#         b.append(a[c])
# print(b)



# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте в new_list. Если my_list [1,2,3,4], то new_list [2,3,4,1]

# my_list = [1,2,3,4]
# new_list = [my_list[-1]]+my_list[:-1]
# print(my_list)
# print(new_list)

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

# my_list = [1,2,3,4]
# a = my_list.pop(0)
# print(a)
# my_list.append(1)
# print(my_list)

#
# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)
#
# a = "43 больше чем 34 но меньше чем 56"
# b = a.split()
# print(b)
# z = []
# for i in b:
#      if i.isnumeric():
#           z.append(int(i))
# print(z)
# print(sum(z))





# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string"
# l_limit = "o"
# r_limit = "g"
# l = my_str.find(l_limit)
# r = my_str.rindex(r_limit)
# s = my_str[l+1 : r]
# print(s)


#
# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)
# my_str = 'abcde'
# for i in range(len(my_str)):
#     if len(my_str) % 2 != 0:
#         my_str += "_"
# print(my_str)
# my_list = []
# for i in range(0,len(my_str),2):
#     my_list.append(my_str[i:i+2])
# print(my_list)


#
# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

# my_s = [2,4,1,5,3,9,0,7]
# l = []
# for ind in range(1,len(my_s)-1):
#      if my_s[ind] > my_s[ind - 1] + my_s[ind + 1]:
#          l.append(my_s[ind])
#         # print(my_s[ind])
# print(l)
# len_l = len(l)
# print(len_l)

# 10. Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Определить возраст самого молодого человека и поместить в новый список имена всех людей,
# чей возраст совпадает с этим минимальным возрастом.
# б) Определить самое длинное имя и поместить в новый список имена всех людей,
# чье имя по длине совпадает с этой длиной.
# в) Посчитать среднее количество лет всех людей из списка.

# persons = [{"name": "John", "age": 12},
#      {"name": "Max", "age": 6},
#      {"name": "Mike", "age": 52},
#      {"name": "Natali", "age": 5},
#      {"name": "Nasty", "age": 5},
#      {"name": "Anna", "age": 29}]
#
# age_min = persons[0]["age"]
# for human in persons:
#      if human["age"]< age_min:
#           age_min = human["age"]
# print(f"Min age - {age_min} years")
#
# names_min_age = []
# for human in persons:
#      if human["age"]== age_min:
#           names_min_age.append(human["name"])
# print(f"Names person with min age - {names_min_age}")
#
# max_long_name = len(persons[3]["name"])
# names_longest = []
# for human in persons:
#      if len(human["name"]) > max_long_name:
#           max_long_name = len(human["name"])
#
# this_name = []
# for human in persons:
#      if max_long_name == len(human["name"]):
#           this_name.append(human["name"])
# print(f"The longest name is - {this_name}")
#
# age = []
# for human in persons:
#      age.append(human["age"])
# middle_age = sum(age)/ len(age)
# print(f"Middle age our persons = {middle_age} years")

