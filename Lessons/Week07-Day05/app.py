# # 1
# y = 0
# def func(list1):
#    return y
# list1 = (8, 2, 3, 0, 7) 
# for i in list1:
#         y += i
# print(y)


# # 2
# def func(list1):
#     y = 1
#     for i in list1:
#         y = y*i
#     print(y)
# list2 = [8, 2, 3, -1, 7]
# func(list2)


# # 3
# def returnDay(x):
#     if 1 <= x <= 7:
#         if x == 1:
#             print('1 is Sunday')
#         elif x == 2:
#             print('2 is Monday')
#         elif x == 3:
#             print('3 is Tuesday')
#         elif x == 4:
#             print('4 is Wednesday')
#         elif x == 5:
#             print('5 is Thursday')
#         elif x == 6:
#             print('6 is Friday')
#         elif x == 7:
#             print('7 is Saturday')
#     else:
#         return None
# x = int(input('Day: '))
# returnDay(x)
        
    

# # 4
# def lastElement(list1):
#     if list1:
#         return list1[-1]
#     return None
# list1 = [1,2,3]
# list2 = []
# print(lastElement(list1))
# print(lastElement(list2))


# 5
# def evenElement(list1):
#     for i in list1:
#         if i%2 == 0:
#             print(i, end=' ' )
# list1 = [1,2,3,4,5,6,7,8,9,10]
# evenElement(list1)


# 6
# def showEmploye():
#       print(name,salary)

# showEmployee(name=input())



# 7
def func(*list1):
    y = 0
    for x in list1:
        y = y + x
    return y
print(func(8, 2, 3, 0, 7))
