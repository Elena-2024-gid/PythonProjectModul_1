grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(list(students))
journal = {}
for i in range(0, len(grades)):
    mean = sum(grades[i]) / len(grades[i])
    journal[students_list[i]] = mean
print(journal)






