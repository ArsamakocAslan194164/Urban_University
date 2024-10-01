grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = {}#Создаем словарь


students = sorted(students)# Преобразоввываем в список и сортируем по алфавиту

def average(numbers):# Функция вычисления среднего бала
    if len(numbers) == 0:
        return 0  # Проверка на случай, если список пуст
    return sum(numbers) / len(numbers)

grades[0] = average(grades[0])
grades[1] = average(grades[1])
grades[2] = average(grades[2])
grades[3] = average(grades[3])
grades[4] = average(grades[4])


students_list = {students[0]: grades[0],
                 students[1]: grades[1],
                 students[2]: grades[2],
                 students[3]: grades[3],
                 students[4]: grades[4]}

print(students_list)



