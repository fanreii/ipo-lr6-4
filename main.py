'''Написать программу, которая:
- Запрашивает у пользователя строку для поиска.
- Находит и выводит все строки, которые содержат искомую подстроку, а также их количество из следующего файла.    
- Сортирует найденные строки в порядке их длины (от самой короткой к самой длинной) и выводит их.'''
# запрашивает искомую строку
needed_string = input ("Введите искомую строку: ")
# открыте файла text.txt
with open('text.txt', 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
# поиск искомой строки
matching_lines = []
for line in lines:
    if needed_string in line:
        matching_lines.append(line.strip())
# вывод количества найденных строк
print("Количество найденных строк: ", len(matching_lines))
# вывод найденных строк
for line in matching_lines:
    print(line)
# сортировка строк по длине
sorted_lines = sorted(matching_lines, key = len)
# вывод отсортированных строк
print("Отсортированные по длине строки: ")
for line in sorted_lines:
    print(line)
