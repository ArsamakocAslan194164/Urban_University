#Работа со словорями
print("\nРабота со словорями! \n")
my_dict = {"Григорий": 1996, "Арсен": 1980, "Екатерина": 1990} #Создаем словарь
print(my_dict)
print(my_dict["Григорий"])#Ищем год рождение по ключу Григорий
#Добавляем два новых элемента в словарь, так же можно добавить по одному используя my_dict ["Николай"] = 1995 и my_dict ["Роза"] = 1998
my_dict.update({"Николай": 1995,
                "Роза": 1998})
print(my_dict)
#Удаляем Григорий и выводим удаленное значение на экран
print("Удаление 'Григорий' прошло успешно:",my_dict.pop("Григорий"))
print(my_dict)

#Работа со множествами
print("\nРабота со множествами! \n")

my_set = {1, 2, 3, 4, 1, 2, 3, 4, 5, (1, 2, 3), 'Тест', True}
print(my_set)
print("Добавляем 6 и 7:", my_set.add(6), my_set.add(7))
print(my_set)
print("Удаляем 1 и 2", my_set.remove(1), my_set.remove(2))
print(my_set)