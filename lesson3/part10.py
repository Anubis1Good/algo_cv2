employee_numbers = [2, 9, 18, 28]
employee_names = ["Дима", "Марина", "Андрей", "Никита"]

# упаковка двух последовательностей в одну
zipped_values = zip(employee_names, employee_numbers)
zipped_list = list(zipped_values)

print(zipped_list)
print(zipped_list[::-1])

employees_zipped = [('Дима', 2), ('Марина', 9), ('Андрей', 18), ('Никита', 28)]
# распаковка одной последовательности в две
employee_names, employee_numbers = zip(*employees_zipped)

print(employee_names)
print(employee_numbers)