grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
f = [len(grades[0]), len(grades[1]), len(grades[2]), len(grades[3]), len(grades[4])]  #Считает количество содержащих чисел в списке
k = [sum(grades[0]), sum(grades[1]), sum(grades[2]), sum(grades[3]), sum(grades[4])]  #Считает сумму содержащих чисел в списке
grade = [k[0] / f[0], k[1] / f[1], k[2] / f[2], k[3] / f[3], k[4] / f[4]]   #Считает Средеию сумму содержащих чисел в списке

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
stud = list(students)  #Перевод в другой тип
stud.sort() #Сортирует множество по порядку Алфавита

each_students_average_score = dict(zip(stud, grade)) #Делает словарь(dict) из двух списков
print(each_students_average_score)

print(type(grade))