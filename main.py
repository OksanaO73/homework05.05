grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
print(students)
students.sort()
print(students)
d = dict(zip(students, grades))
print(d)
grades[0] = sum(grades[0]) / len(grades[0])
grades[1] = sum(grades[1]) / len(grades[1])
grades[2] = sum(grades[2]) / len(grades[2])
grades[3] = sum(grades[3]) / len(grades[3])
grades[4] = sum(grades[4]) / len(grades[4])
print(grades)
d = dict(zip(students, grades))
print(d)

#print(sum(grades)/?)
#avverage1 = sum(grades[1]) / len(grades[1])





# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
