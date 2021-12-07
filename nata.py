
# a = input("Введите слово:")
# for i in range (-1,-len(a)-1,-1):
#     print(a[i],end=(" "))


# n = 5
# for i in range(0,n):
#     print("*"*i)
#     continue
# for i in range(n,0,-1):
#     print("*"*i)


# a = int(input("Введите число а:"))
# b = int(input("Введите число b:"))
# if a > b:
#     for i in range(a,b-1,-1):
#         print(i, end=" ")
# elif a < b:
#     for c in range (a,b+1,1):
#         print(c, end=" ")
# else:
#     print(a)

a = int(input("Введите число а:"))
b = int(input("Введите число b:"))
while not(a < b):
    print("incorect input")
    a = int(input("Введите число а:"))
    b = int(input("Введите число b:"))
    continue
for i in range (a,b+1):
    print(i, end=" ")

