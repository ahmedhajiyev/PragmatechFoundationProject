# 1
# list = [1, 2, 3, 4, 5, 6, 7]
# y = 0
# for i in list:
#     y += i
# print(y)


# 2
# list = [1, 2, 3, 7, 5, 4]
# list.sort()
# print(list[-1])


# 3
# list = [2, 1, 3, 7, 5, 4]
# list.sort()
# print(list[0])


# # 4
# list = ['abc', 'xyz', 'aba', '1221']
# for x in list:
#     if len(x) >= 2 and x[0] == x[-1]:
#         print(x)


# # 5
# list = []
# if not list:
#     print('Empty')
# else:
#     print('not empty')


# 6
# foods = ("coconut", "walnut", "carrot", "broccoli", "onion")  
# for i in foods:
#     print('Foods: ' + i)
# # foods[0] = "tomatoes "
# print(foods)
# foods = list(foods)
# foods[1] = "patatoes "
# foods[2] = "eggs "
# foods = tuple(foods)
# for x in foods:
#     print("Foods: " + x)


# 7
list = ["Resad","Elxan","Rasim","admin","Nicat"]

for name in list:
    if name == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again.")