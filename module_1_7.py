immutable_var = 1, 2, "Имя", "Фамилия", 1.2
print(immutable_var)
# Кордежи не изменяются
# immutable_var[0] = 4

#  File "C:\Users\arsam\PycharmProjects\Urban_University\module_1_7.py", line 4
#    immutable_var[0] = 4
#IndentationError: unexpected indent
#
#Process finished with exit code 1

mutable_list = [0, 1, 2 ,3.3, "имя", "Фамилия"]
print(mutable_list)
mutable_list[0] = 99
print(mutable_list[0])