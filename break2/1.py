# # break, continue, else
# #
# # break - прерывает любой цикл
# #
# # n = int(input())
# # flag = False
# # for i in range(n):
# #     x = int(input())
# #     if x == 10:
# #         flag = True
# #         break
# #
# # if flag == True:
# #     print('Урааа')
# # else:
# #     print('yyyyy')
# #
# # print('Урааа' if flag == True else 'yyyy')
# #
# #
# #
# #
# # n = int(input())
# # for i in range(n):
# #     x = int(input())
# #     if x == 10:
# #         print('Урааа')
# #         break
# # else:
# #     print('yyyyy')
# #
# # continue - переводит к следующей итерации цикла
# #
# n = int(input())
# for i in range(n):
#     x = int(input())
#     if x == 2 or x == 3:
#         continue
#     else:
#         print(x)
#
# вложенные циклы
Это цикл в цикле
#
for h in range(24):
    for m in range(60):
        if m == 5:
            break
        for s in range(60):
            print(f'{h} : {m} : {s}')
